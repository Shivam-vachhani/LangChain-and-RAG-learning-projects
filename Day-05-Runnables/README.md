# 🦜 LangChain – Day 05: Runnables

Day 5 went deeper into LangChain's **Runnable primitives** — the building blocks behind every chain. Instead of using the `|` pipe shorthand, this day was about understanding what's actually happening under the hood.

---

## 🔗 RunnableSequence
Used `RunnableSequence` explicitly to wire steps together in order — same as the `|` pipe but more verbose and intentional. Good for understanding that every chain is just a sequence of runnables executing one after another.

## ⚡ RunnableParallel
Ran multiple chains on the same input at the same time — generated both a **guide** and a **review** for a game in a single `invoke()` call. Each key in the dict is an independent chain running in parallel, results come back together as a dict.

## 🔀 RunnableBranch + RunnablePassthrough
Built a smart summarizer — generates a report, then **checks the word count**. If the report exceeds 500 words it gets summarized, otherwise it passes through unchanged using `RunnablePassthrough()`. Clean way to add conditional logic without always running every step.

## 🛠️ RunnableLambda
Wrapped a plain Python function (`word_count`) into the chain using `RunnableLambda` — no LLM needed, just custom logic slotted directly into the pipeline. Combined with `RunnableParallel` and `RunnablePassthrough` to output the joke, its explanation, and its word count all at once.

---

*Stack: LangChain · OpenAI*