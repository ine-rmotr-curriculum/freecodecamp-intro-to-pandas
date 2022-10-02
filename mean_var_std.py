import numpy as np

def calculate(list) : 

    try : 
        a = np.array(list)
        a = a.reshape(3,3)
        
        calculations = {
        'mean' : [],
        'variance' : [], 
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
        }

        fl = a.flatten()
        calculations['mean'].extend([np.mean(a, axis = 0).tolist(), np.mean(a, axis = 1).tolist(), np.mean(fl).tolist()])
        calculations['variance'].extend([np.var(a, axis = 0).tolist(), np.var(a, axis = 1).tolist(), np.var(fl).tolist()])
        calculations['standard deviation'].extend([np.std(a, axis = 0).tolist(), np.std(a, axis = 1).tolist(), np.std(fl).tolist()])
        calculations['max'].extend([np.max(a, axis = 0).tolist(), np.max(a, axis = 1).tolist(), np.max(fl).tolist()])
        calculations['min'].extend([np.min(a, axis = 0).tolist(), np.min(a, axis = 1).tolist(), np.min(fl).tolist()])
        calculations['sum'].extend([np.sum(a, axis = 0).tolist(), np.sum(a, axis = 1).tolist(), np.sum(fl).tolist()])


        return calculations

    except ValueError as ve:
        print(ve)
        print("List must contain nine numbers." )

calculate([1,2,3,4,5,6,7])
