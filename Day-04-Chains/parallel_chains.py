from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task='text-generation',
    max_new_tokens=1024,
    top_k=30,
    temperature=0.1
)

model1 = ChatOpenAI(model='gpt-4o-mini')

model2 = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template='Genrate note on given text : \n {text}',
    input_variables=['text']
)

template2 = PromptTemplate(
    template = ('Genreate 5 question on given text: \n {text}'),
    input_variables= ['text']
)

template3 = PromptTemplate(
    template=('Merge the given documents notes -> {notes} and quiz -> {quiz}'),
    input_variables=['notes','quiz']
)

parser = StrOutputParser()


text = """ World War II,pip or the Second World War (1 September 1939, 2 September 1945), was a global conflict between two coalitions: the Allies and the Axis powers. Nearly all of the world's countries participated. Tanks and aircraft played major roles, the latter enabling the strategic bombing of cities and delivery of the only nuclear weapons used in war. World War II was the deadliest conflict in history, causing the death of 60 to 75 million people. Millions died as a result of massacres, starvation, disease, and genocides, including the Holocaust. After the Allied victory, Germany, Austria, Japan, and Korea were occupied, and German and Japanese leaders were tried for war crimes.

The causes of World War II included unresolved tensions in the aftermath of World War I and the rise of fascism in Europe and militarism in Japan. Key events preceding the war included Japan's invasion of Manchuria in 1931, the Spanish Civil War, the outbreak of the Second Sino-Japanese War in 1937, and Germany's annexations of Austria and the Sudetenland. World War II is generally considered to have begun on 1 September 1939, when Nazi Germany, under Adolf Hitler, invaded Poland, after which the United Kingdom and France declared war on Germany. Poland was also invaded by the Soviet Union in mid-September and was partitioned between Germany and the Soviet Union under the Molotov–Ribbentrop Pact. In 1940, the Soviet Union annexed the Baltic states and parts of Finland and Romania, while Germany conquered Norway, Denmark, Belgium, Luxembourg, and the Netherlands. After the fall of France in June 1940, the war continued mainly between Germany, now assisted by Fascist Italy, and the British Empire and British Commonwealth, with fighting in the Balkans, Mediterranean, Middle East, East Africa, the aerial Battle of Britain, the Blitz, and the naval Battle of the Atlantic. By mid-1941, Yugoslavia and Greece had also been defeated by Axis countries. In June 1941, Germany invaded the Soviet Union, opening the Eastern Front.

In December 1941, Japan attacked American and British territories in Asia and the Pacific, including Pearl Harbor in Hawaii, leading the United States to enter the war against the Axis. Japan conquered much of coastal China and Southeast Asia, but its advances in the Pacific were halted in June 1942 at the Battle of Midway. In early 1943, Axis forces were defeated in North Africa and at Stalingrad in the Soviet Union. An Allied invasion of Italy in July resulted in the fall of its fascist regime, and Allied offensives in the Pacific and the Soviet Union forced the Axis to retreat on all fronts. In 1944, the Western Allies invaded France at Normandy, and the Soviet Union advanced into Central Europe. Japan also suffered major setbacks including the crippling of its navy by the United States, the loss of key Western Pacific islands, and defeats in Burma.

The war in Europe concluded with the liberation of German-occupied territories and the invasion of Germany by the Allies, which culminated in the fall of Berlin to Soviet troops and Germany's unconditional surrender on 8 May 1945. On 6 and 9 August, the US dropped atomic bombs on Hiroshima and Nagasaki followed by a Soviet invasion of Japanese-occupied Manchuria. Japan announced its unconditional surrender on 15 August and signed a surrender document on 2 September 1945. World War II transformed the political, economic, and social structures of the world, and established the foundation of international relations for the rest of the 20th century and into the 21st century. The United Nations was created to foster international cooperation and prevent future conflicts, with the victorious great powers—China, France, the Soviet Union, the UK, and the US—becoming the permanent members of its Security Council. The Soviet Union and the US emerged as rival superpowers, setting the stage for the Cold War. In the wake of Europe's devastation, the influence of its great powers waned, triggering the decolonisation of Africa and of Asia. Many countries whose industries had been damaged moved towards economic recovery and expansion. """


parallel_chain = RunnableParallel({
    'notes': template1 | model2 | parser,
    'quiz': template2 | model1 | parser
})

merge_chain = template3 | model2 | parser

final_chain = parallel_chain | merge_chain 

result = final_chain.invoke({'text': text })

print(result)

final_chain.get_graph().print_ascii()