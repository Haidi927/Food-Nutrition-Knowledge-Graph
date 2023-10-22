The COVID-19 pandemic has made us pay more attention to our health than ever before. A balanced diet is an essential component of ensuring good health. The Food Nutrition Knowledge Graph (FNKG) aims to provide users with professional dietary advice.
# The Construction of Food Nutrition Knowledge Graph
As shown in the figure below, the construction of FNKG consists of six parts: data integration, patterns design, data processing, data fusion, data storage and visualization.
![The Framework of FNKG](https://github.com/Haidi927/Food-Nutrition-Knowledge-Graph/blob/main/picture/The%20Framework%20of%20FNKG.png)
## 1. Data Integration
"Food Nutrition", as a national planning textbook for higher education in China, focuses on the nutritional value of food, dietary nutrition and health, systematically expounds the basic theories and practical application knowledge and methods of food nutrition, integrating food and diet throughout the book. We selected "Food Nutrition" as the primary data source for FNKG.  
  
  The "Chinese Food Composition Table" was published by Peking University Medical Press. It covers the nutritional composition data of existing plant foods, animal foods and partial industry foods in China. FNKG selected it as a quantitative indicator to achieve more accurate recommendations.  
  
  FNKG crawled nutrition website data, such as [China Health Network](https://www.zhys.com/), [Food Partner Network](http://foodmate.net/), and [Baike](https://baike.baidu.com/) to supplement food nutrition data.

## 2. Patterns Design
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

## 3. Data Alignment*  
From the data sources described in the ***Data Integration***, we have integrated multiple accessible databases, including the manually constructed [FNKG pattern database](https://github.com/Haidi927/Food-Nutrition-Knowledge-Graph/blob/main/dataset/demo_dataset.csv), the food nutrient content database constructed by automated tools, and [Ta-da-recipe-dataset](https://github.com/Eimo-Bai/Ta-da-recipe-dataset).  
  
  **In future work, FNKG needs to integrate these three heterogeneous databases to achieve better quantitative reasoning.**
## 4. Visualization*  
FNKG aims to provide advice to a wide range of people who need professional dietary advice, so it needs to provide visualization methods that meet the habits of all age groups.  

  
**In future work, FNKG will be released in the form of a product, with the purpose of privately customized AI nutritionists to record people's eating habits, provide dietary advice, and ensure a healthy life.**



# Demonstration
A simple query demo.
| Question| Query| Return|
| ------ | ------ |------ |
|What are all the foods or nutrients that affect cardiovascular disease?|`MATCH (disease:disease{name:“cardiovascular disease”})-[r]->(factors)` RETURN disease, factors|![simple_query](https://github.com/Haidi927/Food-Nutrition-Knowledge-Graph/blob/main/picture/simple_query.png)|


  
![lab](https://github.com/Haidi927/Food-Nutrition-Knowledge-Graph/blob/main/picture/lab.png)
