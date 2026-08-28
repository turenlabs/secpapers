const SORTS = new Set(["newest", "updated", "relevance", "title"])
const PAPER_STRING_FIELDS = [
  "id",
  "title",
  "excerpt",
  "primary_category",
  "published",
  "updated",
  "url",
  "pdf_url",
]
const PAPER_ARRAY_FIELDS = ["authors", "topics", "categories"]

export const DEFAULT_VIEW_STATE = Object.freeze({
  query: "",
  topic: "all",
  sort: "newest",
})

export function normalizeText(value) {
  return String(value ?? "")
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^\p{Letter}\p{Number}]+/gu, " ")
    .trim()
}

export function parseViewState(search, validTopics = new Set()) {
  const params = new URLSearchParams(search)
  const topic = params.get("topic") ?? DEFAULT_VIEW_STATE.topic
  const sort = params.get("sort") ?? DEFAULT_VIEW_STATE.sort

  return {
    query: (params.get("q") ?? "").trim().slice(0, 200),
    topic: validTopics.has(topic) ? topic : DEFAULT_VIEW_STATE.topic,
    sort: SORTS.has(sort) ? sort : DEFAULT_VIEW_STATE.sort,
  }
}

export function serializeViewState(state) {
  const params = new URLSearchParams()
  if (state.query) params.set("q", state.query)
  if (state.topic !== DEFAULT_VIEW_STATE.topic) params.set("topic", state.topic)
  if (state.sort !== DEFAULT_VIEW_STATE.sort) params.set("sort", state.sort)
  const query = params.toString()
  return query ? `?${query}` : ""
}

export function isValidIndexPayload(payload) {
  if (
    payload?.schema_version !== 1 ||
    !Array.isArray(payload.papers) ||
    !Array.isArray(payload.topics) ||
    !Array.isArray(payload.publication_years) ||
    (payload.latest_update !== null && typeof payload.latest_update !== "string")
  ) {
    return false
  }

  return payload.topics.every(isValidTopic) && payload.papers.every(isValidPaper)
}

export function filterAndSort(papers, state) {
  const terms = normalizeText(state.query).split(" ").filter(Boolean)
  const matching = papers.filter((paper) => {
    if (state.topic !== "all" && !paper.topics.includes(state.topic)) return false
    if (!terms.length) return true
    const haystack = searchText(paper)
    return terms.every((term) => haystack.includes(term))
  })

  return matching.sort(comparator(state.sort))
}

export function countRecentPapers(papers, days = 30) {
  if (!papers.length) return 0
  const newest = Math.max(...papers.map((paper) => Date.parse(paper.published)))
  const cutoff = newest - days * 24 * 60 * 60 * 1000
  return papers.filter((paper) => Date.parse(paper.published) >= cutoff).length
}

export function monthlyActivity(papers, months = 12) {
  if (!papers.length) return Array.from({ length: months }, () => 0)
  const latest = new Date(Math.max(...papers.map((paper) => Date.parse(paper.published))))
  const buckets = Array.from({ length: months }, () => 0)

  papers.forEach((paper) => {
    const published = new Date(paper.published)
    const offset =
      (latest.getUTCFullYear() - published.getUTCFullYear()) * 12 +
      latest.getUTCMonth() -
      published.getUTCMonth()
    if (offset >= 0 && offset < months) buckets[months - offset - 1] += 1
  })

  return buckets
}

function searchText(paper) {
  return normalizeText(
    [
      paper.title,
      paper.authors.join(" "),
      paper.topics.join(" "),
      paper.categories.join(" "),
      paper.excerpt,
      paper.abstract,
    ].join(" "),
  )
}

function isValidTopic(topic) {
  return (
    typeof topic?.id === "string" &&
    typeof topic.name === "string" &&
    Number.isInteger(topic.count)
  )
}

function isValidPaper(paper) {
  return (
    PAPER_STRING_FIELDS.every((field) => typeof paper?.[field] === "string") &&
    PAPER_ARRAY_FIELDS.every((field) => Array.isArray(paper?.[field])) &&
    Number.isInteger(paper.relevance_score)
  )
}

function comparator(sort) {
  if (sort === "title") {
    return (left, right) => left.title.localeCompare(right.title)
  }
  if (sort === "relevance") {
    return (left, right) =>
      right.relevance_score - left.relevance_score || newestFirst(left, right)
  }
  if (sort === "updated") {
    return (left, right) => right.updated.localeCompare(left.updated) || newestFirst(left, right)
  }
  return newestFirst
}

function newestFirst(left, right) {
  return right.published.localeCompare(left.published) || right.updated.localeCompare(left.updated)
}
