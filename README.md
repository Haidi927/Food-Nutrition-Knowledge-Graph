# Knowledge-Graph-Construction-for-Food-Nutrition

In this study, Food Nutrition, China Food Composition List, and Baidu Encyclopedia were used as data sources to design a framework for constructing food nutrition knowledge graph by constructing 7 types of node labels and 15 types of relationships.
Its pattern layer is as follows:
![pattern_lay](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/pattern%20layer.png)
Taking the "cardiovascular disease" node as an example, the query results through the command: "MATCH (a:disease{name:"cardiovascular disease")-[r]->(b) RETURN a,b" are as shown in the figure. Through the query, it can be found that nutrients such as "coenzyme q10", "oleic acid" and "arginine" are beneficial to "cardiovascular diseases". Foods such as "spinach" and "cauliflower" are rich in these nutrients and are also good for "cardiovascular diseases", while foods such as "cream", "egg yolk" and "pork" are not good for "cardiovascular diseases". And the special group of "elderly people" are prone to such diseases and should pay attention to a healthy diet.
![sample](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/semple.png)
Due to the unpublished paper and the confidentiality of the project, we have only published a part of the data as a formal presentation. We have not yet published complete data in the dataset. The complete dataset and the construction method will be fully disclosed after the publication of the paper.
This team is from the Data Science and Knowledge Engineering Laboratory of Zhengzhou University of Light Industry.
![lab](https://github.com/haidisuper/Knowledge-Graph-Construction-for-Food-Nutrition/blob/main/lab.png)
