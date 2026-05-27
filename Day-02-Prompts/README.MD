# 🦜 LangChain – Day 02: Prompts

Day 2 was all about **Prompt Engineering in LangChain** — how to structure, template, and manage prompts properly. Also built a real mini project with a Streamlit UI.

---

## 💬 Chatbot with Memory

Built a terminal chatbot (`chatbot_demo.py`) using `ChatOpenAI` and LangChain message types — `SystemMessage`, `HumanMessage`, `AIMessage`. The key insight: passing the full `chat_history` list on every `.invoke()` call is what gives the model memory. Without it, every message is a fresh conversation.

## 📝 Prompt Templates

Explored two types of prompt templates:

- **`PromptTemplate`** — for simple single-input prompts with `{placeholder}` variables.
- **`ChatPromptTemplate`** — for structured chat-style prompts with system + human turns, each with their own variables like `{domain}` and `{topic}`.

Templates make prompts reusable, clean, and dynamic instead of hardcoded strings.

## 🔁 MessagesPlaceholder

Used `MessagesPlaceholder` inside a `ChatPromptTemplate` to inject an entire conversation history into a prompt at runtime. This is how you'd wire up a real stateful chatbot — load past messages, slot them in, then append the new query.

## 💾 Saving & Loading Prompts

Saved a `PromptTemplate` to `template.json` using `.save()` and reloaded it later with `load_prompt()`. This lets you version and reuse prompts across different scripts or projects without redefining them.

## 🚀 Mini Project — Research Paper Summarizer

Built a Streamlit app (`prompt_ui.py`) that lets you pick a research paper, explanation style, and length from dropdowns — then generates a structured summary using the saved prompt template. First real end-to-end project combining prompts + LLM + UI.

---

_Stack: LangChain · OpenAI · Streamlit_
