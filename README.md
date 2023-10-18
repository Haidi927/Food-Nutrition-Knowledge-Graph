The COVID-19 pandemic has made us pay more attention to our health than ever before. A balanced diet is an essential component of ensuring good health. The Food Nutrition Knowledge Graph (FNKG) aims to provide users with professional dietary advice.
# The Construction of Food Nutrition Knowledge Graph
As shown in the figure below, the construction of FNKG consists of six parts: data integration, patterns design, data processing, data fusion, data storage and visualization.
![process diagram](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/process%20diagram.png)
## 1.Data Integration
"Food Nutrition", as a national planning textbook for higher education in China, focuses on the nutritional value of food, dietary nutrition and health, systematically expounds the basic theories and practical application knowledge and methods of food nutrition, integrating food and diet throughout the book. We selected "Food Nutrition" as the primary data source for FNKG.  
The "Chinese Food Composition Table" was published by Peking University Medical Press. It covers the nutritional composition data of existing plant foods, animal foods and partial industry foods in China. FNKG selected it as a quantitative indicator to achieve more accurate recommendations.  
FNKG crawled nutrition website data, such as [China Health Network](https://www.zhys.com/), [Food Partner Network](http://foodmate.net/), and [Baike](https://baike.baidu.com/) to supplement food nutrition data.

## 2.Patterns Design
Extract, process, and annotate data to build a corpus.  
  
| Definition    | Concept    |sample|
| ------ | ------ |------ |
|Nutrients| substances with nutritional functionality |protein|
| non-nutrients | do not have a direct role in maintaining growth and development  |Dietary fiber|
| disease  | a process in which abnormal life activities occur due to disorders of the body's homeostasis regulation system under certain etiological conditions  |diabetes|
| food | Substances that supply nutrients and energy needed by organisms to maintain life and promote growth and development.  |milk|
| special populations  | Groups of people distinguished based on certain characteristics, such as age, gender, physical fitness, etc.  |infants|
| symptom  | The manifestation of a disease, disorder, or abnormal condition  |stomach ache|
| organ | Nutrients, organs, functions, and tissues that non-nutrients act on |heart|

 
## 3.Model Design:
Focus on nutrition, diseases, and demographics, constructing 7 node labels and 15 relationship types, with a designed pattern layer。

## 4.Data Fusion:
Address entity heterogeneity issues by designing an entity alignment algorithm based on the attribute of entities being resistant to change, using cosine similarity of word vectors to determine if they represent the same entity.

## 5.Data Storage:
Employ the Neo4j graph database to store nutritional data.    
Transform and import data into CSV format, utilizing Python's py2neo functions for entity and relationship creation.

## 6.Visualization and Recommendations:
Support basic queries and progressive retrieval.

Its pattern layer is as follows:
![pattern_lay](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/pattren_lay.png)

## This is a simple query demo. 
Take the "cardiovascular disease" node as an example, and query with the command: "MATCH (a:disease{name:“cardiovascular disease”})-[r]->(b) RETURN a,b."
![sample](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/sample.png)


For elderly individuals prone to cardiovascular ailments, it is recommended to include flavonoid-rich foods like hawthorn and pineapple in their diet. However, if diabetes, a prevalent condition among the elderly, coexists, pineapple consumption should be avoided. Notably, cardiovascular disease may manifest as a complication of iron-deficiency anemia. Supplementation with iron and vitamin C-enriched spinach can effectively curb iron-deficiency anemia and diminish the occurrence of cardiovascular disease.

## This is a example of a progressive query.

Take the "phosphatidylcholine" node as an example, and query with the command: "MATCH (a:Nutrient{name:“phosphatidylcholine”) RETURN a". It can be observed that phosphatidylcholine is classified within the lipid category.
![sample_1](https://github.com/Haidi927/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/sample_1.png)

it is considered as the "third nutrient" alongside proteins and vitamins, yet it is not well-known among the public. Double-clicking on this node creates a subgraph centered around phosphatidylcholine.

![sample_2](https://github.com/Haidi927/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/sample_2.png)
Analysis of the graph indicates that phosphatidylcholine is abundant in food sources such as egg yolks, milk, and soybeans. Recommending increased consumption of phosphatidylcholine-rich foods for the elderly and infants, and advocating moderation for individuals with diabetes and hyperlipidemia, underscores their cardiovascular and neurological benefits. Conversely, caution is advised for patients with gout, who are recommended to abstain from such dietary sources.

![lab](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/lab.png)
