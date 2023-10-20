The COVID-19 pandemic has made us pay more attention to our health than ever before. A balanced diet is an essential component of ensuring good health. The Food Nutrition Knowledge Graph (FNKG) aims to provide users with professional dietary advice.
# The Construction of Food Nutrition Knowledge Graph
As shown in the figure below, the construction of FNKG consists of six parts: data integration, patterns design, data processing, data fusion, data storage and visualization.
![The Framework of FNKG](https://github.com/Haidi927/Food-Nutrition-Knowledge-Graph/blob/main/picture/The%20Framework%20of%20FNKG.png)
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
The fifteen types of relationship of FNKG are shown in the table below.
|Type| Domain  | Range    |Sample|
| ------ | ------ |------ |------ | 
|Be Beneficial To | Food |Disease|Blueberries are beneficial for high blood fat |
|Be Harmful To | Food |Disease|Eggs are harmful for asthma|
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
|Prone to| Special Populations |Disease|Infants is prone to leukemia|
|Alias| Nutrients |Nutrients|Lecithin alias is lecithin|
|Promote Absorption| Nutrients |Nutrients|Vitamins promote absorption of the nutrient iron|  

According to the definition of the entities and the relationships of FNKG, we define the pattern of FNKG as shown in the figure below.
![pattern](https://github.com/Haidi927/Food-Nutrition-Knowledge-Graph/blob/main/picture/pattern.png)  
**Food** and **Disease** and their relationships are the core of the FNKG, where **Food** are composed of **Nutritent** and **Non-nutrient**. The content and function of various nutrients as attributes of **Nutrition** and **Non-nutrition** support the decision-making of **Food** on **Disease**. The **Disease** is the hub of FNKG, which interacts with **Organ**, **Symptom**, and **Population**.

## 3.Data Process



## A simple query demo. 
Take the "cardiovascular" node as an example, and query with the command: "MATCH (a:disease{name:“cardiovascular disease”})-[r]->(b) RETURN a,b." The result is shown below.
![simple_query](https://github.com/Haidi927/Food-Nutrition-Knowledge-Graph/blob/main/picture/simple_query.png)


For elderly individuals prone to cardiovascular ailments, it is recommended to include flavonoid-rich foods like hawthorn and pineapple in their diet. However, if diabetes, a prevalent condition among the elderly, coexists, pineapple consumption should be avoided. Notably, cardiovascular disease may manifest as a complication of iron-deficiency anemia. Supplementation with iron and vitamin C-enriched spinach can effectively curb iron-deficiency anemia and diminish the occurrence of cardiovascular disease.

## A example of a progressive query.

Take the "lecithin" node as an example, and query with the command: "MATCH (a:Nutrient{name:“lecithin”) RETURN a". It can be observed that lecithin is classified within the lipid category.
![progressive_query](https://github.com/Haidi927/Food-Nutrition-Knowledge-Graph/blob/main/picture/progressive_query.png)

Double-clicking on this node creates a subgraph centered around lecithin.

![progressive_query_result](https://github.com/Haidi927/Food-Nutrition-Knowledge-Graph/blob/main/picture/progressive_query_result.png)
Analysis of the graph indicates that foods such as egg yolks, milk, and soybeans are rich in lecithin. The elderly and infants should eat more foods rich in lecithin, and patients with diabetes and hyperlipidemia should also eat more.
These foods are good for your heart and brain. Patients suffering from gout should avoid this food.

![lab](https://github.com/Haidi927/Food-Nutrition-Knowledge-Graph/blob/main/picture/lab.png)
