# 🦜 LangChain – Day 03: Output Parsers

Day 3 focused on **structured outputs** — how to make LLMs return clean, usable data instead of raw text blobs. Also got hands-on with Pydantic for data validation.

---

## 📄 StrOutputParser + Chaining
Started simple — `StrOutputParser` strips the raw `AIMessage` wrapper and gives back a plain string. The more interesting part was chaining: built a two-step pipeline where the model first generates a full report on a topic, then that output flows directly into a second prompt to summarize it — all in one `chain.invoke()` using the `|` pipe operator.

## 🔧 Pydantic Basics
Practiced `pydantic` independently before using it with LangChain — defined a `Student` model with typed fields, optional fields, email validation (`EmailStr`), and range constraints (`Field(gt=0, lt=10)`). Pydantic validates data at runtime and makes it easy to convert between dicts, objects, and JSON.

## 📦 JsonOutputParser
Used `JsonOutputParser` with a `PromptTemplate` — it auto-injects format instructions into the prompt via `partial_variables`, nudging the model to respond in valid JSON. Clean way to get structured data without defining a schema manually.

## ✅ PydanticOutputParser vs `.with_structured_output()`
Explored two approaches for schema-enforced outputs:
- **`PydanticOutputParser`** — older approach, injects schema instructions into the prompt and parses the text response.
- **`.with_structured_output(Person)`** — modern industry standard, directly binds a Pydantic model to the LLM so the output is already a validated Python object. Much cleaner.

## 🗂️ Structured Output — 3 Schema Styles
Compared all three ways to define output schemas for `.with_structured_output()` using a product review as the test case:
- **TypedDict** — simplest, but no runtime validation.
- **Pydantic `BaseModel`** — best for Python, full validation + field constraints.
- **JSON Schema** — best for cross-platform use (e.g. sending structured data between frontend and backend).

---

*Stack: LangChain · OpenAI · HuggingFace · Pydantic*