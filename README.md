The COVID-19 pandemic has made us pay more attention to our health than ever before. A balanced diet is an essential component of ensuring good health. The Food Nutrition Knowledge Graph (FNKG) aims to provide users with professional dietary advice.
# The Construction of Food Nutrition Knowledge Graph
As shown in the figure below, the construction of FNKG consists of six parts: data integration, patterns design, data processing, data fusion, data storage and visualization.
![process diagram](https://github.com/Haidi927/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/The%20Framework%20of%20FNKG.png)
## 1.Data Integration
"Food Nutrition", as a national planning textbook for higher education in China, focuses on the nutritional value of food, dietary nutrition and health, systematically expounds the basic theories and practical application knowledge and methods of food nutrition, integrating food and diet throughout the book. We selected "Food Nutrition" as the primary data source for FNKG.  
The "Chinese Food Composition Table" was published by Peking University Medical Press. It covers the nutritional composition data of existing plant foods, animal foods and partial industry foods in China. FNKG selected it as a quantitative indicator to achieve more accurate recommendations.  
FNKG crawled nutrition website data, such as [China Health Network](https://www.zhys.com/), [Food Partner Network](http://foodmate.net/), and [Baike](https://baike.baidu.com/) to supplement food nutrition data.

## 2.Patterns Design
FNKG defines seven types of entities and fifteen types of relationships.The seven types of entity categories are shown in the table below. 
| Type    | Defination    |Example|
| ------ | ------ |------ |
|Nutrients| Substances with nutritional functionality |Protein|
| Non-nutrients | Substance that does not provide energy but is essential for good health|Dietary fiber|
| Disease  | A state of abnormal body function|Diabetes|
| Food | Substances that  maintain life and promote growth and development  |Milk|
| Populations  | Groups of people distinguished based on certain characteristics  |Infants|
| Symptom  | Discomfort of physical or mental |Stomachache|
| Organ |Body structure that performs function |Heart|  

FNKG is based on **Nutrients** and **Non-nutrients**, and then conducts quantitative analysis of various **Food**. By defining **Populations**, **Organ**, **Symptom**, and **Disease**, for example, FNKG sets the needs or thresholds of **Populations** nutrients for different groups of people to achieve the purpose of providing more scientific dietary advice.  
The seven types of relationship of FNKG are shown in the table below.
|Type| Domain  | Range    |Sample|
| ------ | ------ |------ |------ | 
|Be beneficial to | Food |Disease|Blueberries are beneficial for high blood fat |
|Be harmful to | Food |Disease|Eggs are harmful for asthma|
|Lack | Food |Disease|Lack of nutrient iron can easily lead to iron deficiency anemia |
|Overdose| Food |Disease|Overdose yogurt can easily lead to gastrointestinal diseases |
|Rich| Food |Nutrients|Eggs are rich in protein|
|Rich| Food |Non-nutrients|Apples are rich in dietary fiber|
|Suitable| Food |Special Populations|Purple cabbage is suitable for infants and young children|
|Not Suitable| Food |Special Populations|Skim milk is not suitable for infants|
|Cause| Food |Symptom|Eating grapes and milk at the same time can cause diarrhea|
|Cause| Disease |Symptom|Prediabetes cause dry mouth and tongue|
|Act on| Disease |Organ|Coronary heart disease act on the heart|
|Act on|Symptom |Organ|Abdominal pain often act on the intestines|
|Easy| Special Populations |Disease|Infants is easy to leukemia|
|Alias| Nutrients |Nutrients|Lecithin alias is lecithin|
|Promote absorption| Nutrients |Nutrients|Vitamins promote absorption of the nutrient iron|  

According to the above definition of entities and relationships by FNKG, its Pattern is as shown in the figure below.
![pattern_lay](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/pattren_lay.png)

## 3.Model Design:
Focus on nutrition, diseases, and demographics, constructing 7 node labels and 15 relationship types, with a designed pattern layer。

## 4.Data Fusion:
Address entity heterogeneity issues by designing an entity alignment algorithm based on the attribute of entities being resistant to change, using cosine similarity of word vectors to determine if they represent the same entity.

## 5.Data Storage:
Employ the Neo4j graph database to store nutritional data.    
Transform and import data into CSV format, utilizing Python's py2neo functions for entity and relationship creation.

## 6.Visualization and Recommendations:
Support basic queries and progressive retrieval.



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
