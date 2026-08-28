import assert from "node:assert/strict"
import test from "node:test"

import {
  countRecentPapers,
  filterAndSort,
  isValidIndexPayload,
  monthlyActivity,
  parseViewState,
  serializeViewState,
} from "../docs/search.mjs"

const papers = [
  {
    id: "2608.00001",
    title: "Prompt Injection in Tool-Using Agents",
    authors: ["A. Researcher"],
    published: "2026-08-20T00:00:00Z",
    updated: "2026-08-22T00:00:00Z",
    topics: ["prompt-security", "agent-security"],
    categories: ["cs.CR"],
    excerpt: "A benchmark for indirect attacks.",
    relevance_score: 8,
  },
  {
    id: "2607.00002",
    title: "Private Language Model Inference",
    authors: ["B. Scientist"],
    published: "2026-07-25T00:00:00Z",
    updated: "2026-08-25T00:00:00Z",
    topics: ["privacy"],
    categories: ["cs.CL"],
    excerpt: "Confidential inference for sensitive records.",
    abstract: "Membership inference is evaluated in detail.",
    relevance_score: 5,
  },
  {
    id: "2501.00003",
    title: "Malware Analysis with Language Models",
    authors: ["C. Analyst"],
    published: "2025-01-10T00:00:00Z",
    updated: "2025-01-10T00:00:00Z",
    topics: ["cyber-defense"],
    categories: ["cs.CR"],
    excerpt: "Threat intelligence and malware classification.",
    relevance_score: 6,
  },
]

test("view state accepts known values and rejects unknown topics", () => {
  const state = parseViewState(
    "?q=agent+memory&topic=agent-security&sort=relevance",
    new Set(["all", "agent-security"]),
  )
  assert.deepEqual(state, {
    query: "agent memory",
    topic: "agent-security",
    sort: "relevance",
  })
  assert.equal(parseViewState("?topic=unknown&sort=bad", new Set(["all"])).topic, "all")
})

test("compact payload validation rejects incomplete generated data", () => {
  const webPapers = papers.map((paper) => ({
    ...paper,
    primary_category: paper.categories[0],
    url: `https://arxiv.org/abs/${paper.id}`,
    pdf_url: `https://arxiv.org/pdf/${paper.id}`,
  }))
  const payload = {
    schema_version: 1,
    latest_update: "2026-08-22T00:00:00Z",
    publication_years: ["2026"],
    topics: [{ id: "agent-security", name: "Agent Security", count: 1 }],
    papers: webPapers,
  }
  assert.equal(isValidIndexPayload(payload), true)
  assert.equal(isValidIndexPayload({ ...payload, topics: undefined }), false)
  assert.equal(isValidIndexPayload({ ...payload, papers: [{ id: "broken" }] }), false)
})

test("view state serialization omits defaults", () => {
  assert.equal(serializeViewState({ query: "", topic: "all", sort: "newest" }), "")
  assert.equal(
    serializeViewState({ query: "prompt attack", topic: "privacy", sort: "updated" }),
    "?q=prompt+attack&topic=privacy&sort=updated",
  )
})

test("search covers metadata, excerpts, and lazy abstracts", () => {
  assert.deepEqual(
    filterAndSort(papers, { query: "tool agent", topic: "all", sort: "newest" }).map(
      (paper) => paper.id,
    ),
    ["2608.00001"],
  )
  assert.deepEqual(
    filterAndSort(papers, { query: "membership", topic: "all", sort: "newest" }).map(
      (paper) => paper.id,
    ),
    ["2607.00002"],
  )
  assert.deepEqual(
    filterAndSort(
      [{ ...papers[0], authors: ["周安全"] }],
      { query: "周安全", topic: "all", sort: "newest" },
    ).map((paper) => paper.id),
    ["2608.00001"],
  )
})

test("topic filters and sort modes are deterministic", () => {
  assert.deepEqual(
    filterAndSort(papers, { query: "", topic: "privacy", sort: "newest" }).map(
      (paper) => paper.id,
    ),
    ["2607.00002"],
  )
  assert.deepEqual(
    filterAndSort(papers, { query: "", topic: "all", sort: "updated" }).map(
      (paper) => paper.id,
    ),
    ["2607.00002", "2608.00001", "2501.00003"],
  )
  assert.deepEqual(
    filterAndSort(papers, { query: "", topic: "all", sort: "relevance" }).map(
      (paper) => paper.id,
    ),
    ["2608.00001", "2501.00003", "2607.00002"],
  )
})

test("activity telemetry uses the newest publication as its reference", () => {
  assert.equal(countRecentPapers(papers, 30), 2)
  const activity = monthlyActivity(papers, 12)
  assert.equal(activity.length, 12)
  assert.equal(activity.reduce((sum, count) => sum + count, 0), 2)
  assert.deepEqual(monthlyActivity([], 3), [0, 0, 0])
})
