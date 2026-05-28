from langchain_unstructured import UnstructuredLoader

loader = UnstructuredLoader('dl-curriculum.pdf',
                            strategy='fast',
                            chunking_strategy='basic',
                        )

docs = loader.load()

print(len(docs))
