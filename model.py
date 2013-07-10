import csv

'''
Generate predictive text model/instance using text file

Applied Trie object from Sarath Lakshman

Challenge with using Tries is extensive memory usage
'''

class Trie:
    def __init__(self):
        self.next = {}  #Initialize an empty dict
        self.freq = None #Hold word frequency

    ''' Method to add a string the Trie data structure'''
    def add_item(self, string, frequencies):
        
        if len(string) == 0:
            self.freq = frequencies
            return 
        
        key = string[0] #Extract first character
        string = string[1:] #Capture remaining string

        #If key exists, recurse through remaining string to add
        if self.next.has_key(key):
            self.next[key].add_item(string,frequencies)
        #Else create new trie with key and then add_item() 
        else:
            node = Trie()
            self.next[key] = node
            node.add_item(string,frequencies)

    '''Perform Depth First Search Traversal'''
    def dfs(self, prediction_list, so_far=None):
        
        #If node pointing to empty dict, add word to list
        if self.next.keys() == []:
            prediction_list.append((so_far, self.freq))
            return

        #If node containes a frequency, add word to list
        if self.freq:
            prediction_list.append((so_far, self.freq))

        #Recursively call dfs for all the nodes pointed by keys in the dict
        for key in self.next.keys():
            self.next[key].dfs(prediction_list, so_far+key)

    '''Perform auto completion search on submitted string and return results'''
    def search(self, string, prediction_list, so_far=""):
        
        # Recursively search through string(inital letters submitted) to find starting node to pull words
        if len(string) > 0:
            key = string[0]
            string = string[1:]
            if self.next.has_key(key):
                so_far = so_far + key
                self.next[key].search(string, prediction_list, so_far)
        else:
            #If word has a freq then add to list
            if self.freq:
                prediction_list.append((so_far, self.freq))
            #Depth first search all keys following starting node
            for key in self.next.keys():
                self.next[key].dfs(prediction_list, so_far+key)

        return prediction_list


'''Parse text file and apply to Trie'''
def build_model(file_name):


    #Open file to var so it can be closed
    file_obj = open(file_name)

    #Read file and split values on tab
    row_list = csv.reader(file_obj, delimiter="\t", skipinitialspace=True)

    word_trie = Trie()

    for index, row in enumerate(row_list):
        if index > 0 : #Ignore header colum
            word_trie.add_item(row[1],row[3])    


    file_obj.close()

    return word_trie
 
