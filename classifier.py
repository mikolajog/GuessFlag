from sklearn import tree
import pandas as pd
import graphviz
import csv
import numpy as np
import question_mapper

class Classifier:
    def __init__(self):
        self.current_node = 0

    def read(self, filename, country_list):
        data = []  

        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            for i, row in enumerate(reader):
                if i != 0 and row[0] not in country_list:
                    continue

                datarow = [row[0]] + row[7:]
                data.append(datarow)


        df = pd.DataFrame(data[1:], columns=data[0])
        df.replace('', np.nan, inplace=True)
        df.dropna(inplace=True)
        df = df.drop_duplicates(subset = df.columns[1:])
        self.labels = df['name']
        df = df.drop(['name'], axis=1)
        df_str = df[['mainhue', 'topleft', 'botright']]
        df_str = df_str.apply(lambda x: x.str.strip())

        #this will treat colors in different columns separatly, but it's not a problem
        onehot = pd.get_dummies(df_str, drop_first=True)

        df = df.drop(['mainhue', 'topleft', 'botright'], axis=1)
        df = df.apply(pd.to_numeric)
        self.features = df.join(onehot)

    def fit(self):
        self.clf = tree.DecisionTreeClassifier(criterion='entropy', splitter='best')
        self.clf.fit(self.features, self.labels)

    def export(self):
        dot_data = tree.export_graphviz(self.clf, out_file=None) 
        graph = graphviz.Source(dot_data) 
        graph.render()
        graph.view()

    def is_in_leaf(self):
        return self.clf.tree_.children_left[self.current_node] == self.clf.tree_.children_right[self.current_node]

    def get_question(self):
        _tree = self.clf.tree_
        feature_name = self.features.columns[_tree.feature[self.current_node]]
        threshold = _tree.threshold[self.current_node]
        return (feature_name, threshold)

    def apply_answer(self, is_fulfilled):
        if is_fulfilled:
            self.current_node = self.clf.tree_.children_left[self.current_node]
        else:
            self.current_node = self.clf.tree_.children_right[self.current_node]

    def get_current_labels(self):
        return [label for i, label in enumerate(self.labels) if self.clf.tree_.value[self.current_node][0][i] > 0.5]