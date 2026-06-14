from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()

llm1=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model1=ChatHuggingFace(llm=llm1)

llm2=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
model2=ChatHuggingFace(llm=llm2)

prompt1= PromptTemplate(
    template='generate short and simple notes from the following text \n {text}',
    input_variables=['text']

)

prompt2= PromptTemplate(
    template='generate 3 short question from the following text \n {text}',
    input_variables=['text']
    
)

prompt3= PromptTemplate(
    template='merge the provided notes and quiz into the single document \n {notes} and {quiz}',
    input_variables=['notes','quiz']

)

parser= StrOutputParser()

parellel_chain=RunnableParallel({
    'notes':prompt1 | model1 | parser,
    'quiz':prompt2 | model2 | parser
})

merge_chain= prompt3 | model1 | parser
final_chain= parellel_chain | merge_chain

text="""
A random forest classifier.

A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. Trees in the forest use the best split strategy, i.e. equivalent to passing splitter="best" to the underlying DecisionTreeClassifier. The sub-sample size is controlled with the max_samples parameter if bootstrap=True (default), otherwise the whole dataset is used to build each tree.

For a comparison between tree-based ensemble models see the example Comparing Random Forests and Histogram Gradient Boosting models.

This estimator has native support for missing values (NaNs). During training, the tree grower learns at each split point whether samples with missing values should go to the left or right child, based on the potential gain. When predicting, samples with missing values are assigned to the left or right child consequently. If no missing values were encountered for a given feature during training, then samples with missing values are mapped to whichever child has the most samples.
"""

result=final_chain.invoke({'text':text})
print(result)
