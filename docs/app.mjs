import {
  DEFAULT_VIEW_STATE,
  countRecentPapers,
  filterAndSort,
  isValidIndexPayload,
  monthlyActivity,
  parseViewState,
  serializeViewState,
} from "./search.mjs"

const PAGE_SIZE = 24
const elements = Object.fromEntries(
  [
    "abstract-status",
    "active-context",
    "active-context-label",
    "activity-bars",
    "activity-total",
    "clear-context",
    "clear-search",
    "dialog-abstract",
    "dialog-abstract-status",
    "dialog-arxiv",
    "dialog-authors",
    "dialog-category",
    "dialog-close",
    "dialog-copy",
    "dialog-id",
    "dialog-pdf",
    "dialog-published",
    "dialog-score",
    "dialog-title",
    "dialog-topics",
    "dialog-updated",
    "empty-reset",
    "empty-state",
    "footer-year",
    "load-more",
    "load-more-count",
    "metric-new",
    "metric-topics",
    "metric-total",
    "metric-years",
    "paper-dialog",
    "paper-list",
    "paper-search",
    "paper-sort",
    "paper-template",
    "reset-filters",
    "result-summary",
    "signal-count",
    "signal-date",
    "signal-state",
    "system-status",
    "topic-list",
  ].map((id) => [id, document.getElementById(id)]),
)

const model = {
  abstracts: new Map(),
  abstractsPromise: null,
  abstractsFailed: false,
  papers: [],
  topics: [],
  topicNames: new Map(),
  view: { ...DEFAULT_VIEW_STATE },
  visible: PAGE_SIZE,
}

let currentDialogID = null
let searchTimer = null

boot()

async function boot() {
  bindEvents()
  elements["footer-year"].textContent = new Date().getFullYear()

  try {
    const response = await fetch("./data/papers.json")
    if (!response.ok) throw new Error(`index request failed: ${response.status}`)
    const payload = await response.json()
    if (!isValidIndexPayload(payload)) {
      throw new Error("unsupported paper index")
    }

    model.papers = payload.papers
    model.topics = payload.topics
    model.topicNames = new Map(payload.topics.map((topic) => [topic.id, topic.name]))
    model.view = parseViewState(
      window.location.search,
      new Set(["all", ...payload.topics.map((topic) => topic.id)]),
    )

    elements["paper-search"].value = model.view.query
    elements["paper-sort"].value = model.view.sort
    renderTelemetry(payload)
    renderTopics()
    renderResults()
    openFromHash()
    scheduleAbstractLoad()
  } catch (error) {
    showFatalError(error)
  }
}

function bindEvents() {
  bindCatalogEvents()
  bindDialogEvents()
  bindNavigationEvents()
}

function bindCatalogEvents() {
  elements["paper-search"].addEventListener("input", (event) => {
    window.clearTimeout(searchTimer)
    searchTimer = window.setTimeout(() => {
      model.view.query = event.target.value.trim()
      resetResults(true)
    }, 120)
  })

  elements["paper-sort"].addEventListener("change", (event) => {
    model.view.sort = event.target.value
    resetResults(false)
  })

  elements["clear-search"].addEventListener("click", clearSearch)
  elements["clear-context"].addEventListener("click", () => selectTopic("all"))
  elements["reset-filters"].addEventListener("click", resetAll)
  elements["empty-reset"].addEventListener("click", resetAll)
  elements["load-more"].addEventListener("click", () => {
    model.visible += PAGE_SIZE
    renderResults()
  })

  elements["topic-list"].addEventListener("click", (event) => {
    const button = event.target.closest("button[data-topic]")
    if (button) selectTopic(button.dataset.topic)
  })

  elements["paper-list"].addEventListener("click", (event) => {
    const detail = event.target.closest("button[data-paper]")
    if (detail) openPaper(detail.dataset.paper)
    const topic = event.target.closest("button[data-topic]")
    if (topic) selectTopic(topic.dataset.topic)
  })
}

function bindDialogEvents() {
  elements["dialog-close"].addEventListener("click", () => elements["paper-dialog"].close())
  elements["paper-dialog"].addEventListener("click", (event) => {
    if (event.target === elements["paper-dialog"]) elements["paper-dialog"].close()
  })
  elements["paper-dialog"].addEventListener("close", clearPaperHash)
  elements["dialog-copy"].addEventListener("click", copyPaperLink)
}

function bindNavigationEvents() {
  document.addEventListener("keydown", (event) => {
    const typing = ["INPUT", "SELECT", "TEXTAREA"].includes(document.activeElement?.tagName)
    if ((event.key === "/" && !typing) || (event.key.toLowerCase() === "k" && event.ctrlKey)) {
      event.preventDefault()
      elements["paper-search"].focus()
    }
  })

  window.addEventListener("popstate", restoreViewState)
  window.addEventListener("hashchange", openFromHash)
}

function renderTelemetry(payload) {
  const activity = monthlyActivity(model.papers)
  const maximum = Math.max(...activity, 1)
  const bars = activity.map((count) => {
    const bar = document.createElement("i")
    bar.className = `level-${Math.max(1, Math.ceil((count / maximum) * 10))}`
    return bar
  })

  elements["signal-count"].textContent = model.papers.length.toLocaleString()
  elements["signal-date"].textContent = formatDate(payload.latest_update)
  elements["activity-total"].textContent = activity.reduce((sum, value) => sum + value, 0)
  elements["activity-bars"].replaceChildren(...bars)
  elements["metric-total"].textContent = model.papers.length.toLocaleString()
  elements["metric-topics"].textContent = model.topics.length
  elements["metric-years"].textContent = payload.publication_years.length
  elements["metric-new"].textContent = countRecentPapers(model.papers)
}

function renderTopics() {
  const all = { id: "all", name: "All research", count: model.papers.length }
  const buttons = [all, ...model.topics].map((topic) => {
    const button = document.createElement("button")
    const name = document.createElement("span")
    const count = document.createElement("span")
    button.type = "button"
    button.className = "topic-button"
    button.dataset.topic = topic.id
    button.classList.toggle("active", topic.id === model.view.topic)
    button.setAttribute("aria-pressed", topic.id === model.view.topic ? "true" : "false")
    name.textContent = topic.name
    count.textContent = topic.count.toLocaleString()
    button.append(name, count)
    return button
  })
  elements["topic-list"].replaceChildren(...buttons)
}

function renderResults() {
  const matching = filterAndSort(model.papers, model.view)
  const visible = matching.slice(0, model.visible)
  const cards = visible.map((paper, index) => paperCard(paper, index))
  const remaining = matching.length - visible.length

  elements["paper-list"].replaceChildren(...cards)
  elements["paper-list"].setAttribute("aria-busy", "false")
  elements["paper-list"].hidden = matching.length === 0
  elements["empty-state"].hidden = matching.length !== 0
  elements["load-more"].hidden = remaining <= 0
  elements["load-more-count"].textContent = remaining > 0 ? `${remaining} REMAINING` : ""
  elements["result-summary"].textContent = matching.length
    ? `SHOWING ${visible.length.toLocaleString()} OF ${matching.length.toLocaleString()} SIGNALS`
    : "NO MATCHING SIGNALS"
  renderActiveContext()
}

function paperCard(paper, index) {
  const fragment = elements["paper-template"].content.cloneNode(true)
  const title = fragment.querySelector(".paper-title")
  const inspect = fragment.querySelector(".inspect-paper")
  const topics = paper.topics.slice(0, 3).map((topic) => topicChip(topic, true))

  fragment.querySelector(".paper-number").textContent = String(index + 1).padStart(3, "0")
  fragment.querySelector(".paper-score").textContent = `S/${String(paper.relevance_score).padStart(2, "0")}`
  fragment.querySelector(".paper-date").textContent = formatDate(paper.published)
  fragment.querySelector(".paper-id").textContent = paper.id
  fragment.querySelector(".paper-category").textContent = paper.primary_category
  title.textContent = paper.title
  title.dataset.paper = paper.id
  fragment.querySelector(".paper-authors").textContent = authorLine(paper.authors)
  fragment.querySelector(".paper-excerpt").textContent = paper.excerpt
  fragment.querySelector(".paper-topics").replaceChildren(...topics)
  inspect.dataset.paper = paper.id
  fragment.querySelector(".paper-external").href = paper.url
  return fragment
}

function topicChip(topic, interactive = false) {
  const element = document.createElement(interactive ? "button" : "span")
  element.className = "topic-chip"
  element.textContent = model.topicNames.get(topic) ?? topic
  if (interactive) {
    element.type = "button"
    element.dataset.topic = topic
  }
  return element
}

function renderActiveContext() {
  const parts = []
  if (model.view.topic !== "all") {
    parts.push(`DOMAIN / ${model.topicNames.get(model.view.topic) ?? model.view.topic}`)
  }
  if (model.view.query) parts.push(`QUERY / "${model.view.query}"`)
  elements["active-context"].hidden = parts.length === 0
  elements["active-context-label"].textContent = parts.join("   +   ")
}

function selectTopic(topic) {
  model.view.topic = topic
  resetResults(false)
  renderTopics()
  document.getElementById("catalog").scrollIntoView({ behavior: "smooth", block: "start" })
}

function clearSearch() {
  model.view.query = ""
  elements["paper-search"].value = ""
  resetResults(true)
  elements["paper-search"].focus()
}

function resetAll() {
  model.view = { ...DEFAULT_VIEW_STATE }
  model.visible = PAGE_SIZE
  elements["paper-search"].value = ""
  elements["paper-sort"].value = model.view.sort
  renderTopics()
  renderResults()
  syncViewState(false)
}

function resetResults(replaceHistory) {
  model.visible = PAGE_SIZE
  renderResults()
  syncViewState(replaceHistory)
}

function syncViewState(replace) {
  const url = `${window.location.pathname}${serializeViewState(model.view)}${window.location.hash}`
  window.history[replace ? "replaceState" : "pushState"]({}, "", url)
}

function restoreViewState() {
  model.view = parseViewState(
    window.location.search,
    new Set(["all", ...model.topics.map((topic) => topic.id)]),
  )
  model.visible = PAGE_SIZE
  elements["paper-search"].value = model.view.query
  elements["paper-sort"].value = model.view.sort
  renderTopics()
  renderResults()
}

function scheduleAbstractLoad() {
  const start = () => loadAbstracts().catch(markAbstractFailure)
  if ("requestIdleCallback" in window) {
    window.requestIdleCallback(start, { timeout: 1500 })
    return
  }
  window.setTimeout(start, 400)
}

async function loadAbstracts() {
  if (model.abstractsPromise) return model.abstractsPromise
  elements["abstract-status"].textContent = "Syncing"
  model.abstractsPromise = fetch("./data/abstracts.json")
    .then((response) => {
      if (!response.ok) throw new Error(`abstract request failed: ${response.status}`)
      return response.json()
    })
    .then((payload) => {
      if (payload.schema_version !== 1 || !payload.abstracts) {
        throw new Error("unsupported abstract index")
      }
      model.abstracts = new Map(Object.entries(payload.abstracts))
      model.abstractsFailed = false
      model.papers.forEach((paper) => {
        paper.abstract = model.abstracts.get(paper.id) ?? ""
      })
      elements["abstract-status"].textContent = "Ready"
      if (model.view.query) renderResults()
      if (currentDialogID) renderDialogAbstract(currentDialogID)
    })
  return model.abstractsPromise
}

function openPaper(id, updateHash = true) {
  const paper = model.papers.find((candidate) => candidate.id === id)
  if (!paper) return
  currentDialogID = id
  elements["dialog-id"].textContent = `ARXIV / ${paper.id}`
  elements["dialog-title"].textContent = paper.title
  elements["dialog-authors"].textContent = paper.authors.join(", ")
  elements["dialog-published"].textContent = formatDate(paper.published)
  elements["dialog-updated"].textContent = formatDate(paper.updated)
  elements["dialog-category"].textContent = paper.primary_category
  elements["dialog-score"].textContent = `${paper.relevance_score} / SIGNAL`
  elements["dialog-topics"].replaceChildren(...paper.topics.map((topic) => topicChip(topic)))
  elements["dialog-arxiv"].href = paper.url
  elements["dialog-pdf"].href = paper.pdf_url
  renderDialogAbstract(id)
  if (!elements["paper-dialog"].open) elements["paper-dialog"].showModal()
  if (updateHash) {
    window.history.pushState({}, "", `${window.location.pathname}${window.location.search}#paper=${encodeURIComponent(id)}`)
  }
  loadAbstracts().catch(markAbstractFailure)
}

function renderDialogAbstract(id) {
  const paper = model.papers.find((candidate) => candidate.id === id)
  const abstract = model.abstracts.get(id)
  if (abstract) {
    elements["dialog-abstract"].textContent = abstract
    elements["dialog-abstract-status"].textContent = "Full text ready"
    return
  }
  if (model.abstractsFailed) {
    elements["dialog-abstract"].textContent = `${paper?.excerpt ?? ""} Full abstract index unavailable.`
    elements["dialog-abstract-status"].textContent = "Full text unavailable"
    return
  }
  elements["dialog-abstract"].textContent = `${paper?.excerpt ?? ""} Loading full abstract...`
  elements["dialog-abstract-status"].textContent = "Loading full text"
}

function markAbstractFailure(error) {
  if (model.abstractsFailed) return
  console.error(error)
  model.abstractsFailed = true
  elements["abstract-status"].textContent = "Unavailable"
  if (currentDialogID) renderDialogAbstract(currentDialogID)
}

function openFromHash() {
  const id = paperIDFromHash()
  if (id) {
    openPaper(id, false)
    return
  }
  if (elements["paper-dialog"].open) elements["paper-dialog"].close()
}

function paperIDFromHash() {
  if (!window.location.hash.startsWith("#paper=")) return null
  try {
    return decodeURIComponent(window.location.hash.slice(7))
  } catch {
    return null
  }
}

function clearPaperHash() {
  currentDialogID = null
  if (!paperIDFromHash()) return
  window.history.replaceState({}, "", `${window.location.pathname}${window.location.search}`)
}

async function copyPaperLink() {
  if (!currentDialogID) return
  const link = `${window.location.origin}${window.location.pathname}${window.location.search}#paper=${encodeURIComponent(currentDialogID)}`
  try {
    await navigator.clipboard.writeText(link)
    elements["dialog-copy"].textContent = "COPIED"
    window.setTimeout(() => {
      elements["dialog-copy"].textContent = "COPY LINK"
    }, 1400)
  } catch {
    elements["dialog-copy"].textContent = "COPY FAILED"
  }
}

function formatDate(value) {
  if (!value) return "Unknown"
  return new Intl.DateTimeFormat("en", {
    day: "2-digit",
    month: "short",
    timeZone: "UTC",
    year: "numeric",
  }).format(new Date(value))
}

function authorLine(authors) {
  if (authors.length <= 4) return authors.join(", ")
  return `${authors.slice(0, 4).join(", ")}, et al.`
}

function showFatalError(error) {
  console.error(error)
  elements["paper-list"].setAttribute("aria-busy", "false")
  elements["paper-list"].replaceChildren()
  elements["result-summary"].textContent = "INDEX UNAVAILABLE"
  elements["empty-state"].hidden = false
  elements["empty-state"].querySelector("span").textContent = "INDEX OFFLINE"
  elements["empty-state"].querySelector("h3").textContent = "The research payload could not be loaded."
  elements["empty-state"].querySelector("p").textContent = "Refresh the page or use the Markdown catalog on GitHub."
  elements["empty-reset"].textContent = "RETRY"
  elements["topic-list"].replaceChildren()
  elements["signal-count"].textContent = "OFFLINE"
  elements["signal-date"].textContent = "Unavailable"
  elements["signal-state"].textContent = "OFFLINE"
  elements["system-status"].textContent = "INDEX UNAVAILABLE"
  elements["abstract-status"].textContent = "Offline"
  elements["paper-search"].disabled = true
  elements["paper-sort"].disabled = true
  elements["clear-search"].disabled = true
  elements["reset-filters"].disabled = true
  elements["empty-reset"].addEventListener("click", () => window.location.reload(), { once: true })
}
