import json

def allocate(orderDetails, warehouseDetails):
    orderDetailsJson = json.loads(orderDetails)
    warehouseDetailsJson = json.loads(warehouseDetails)

    tempresults = []
    finalresults = []

    for warehouse in warehouseDetailsJson:
        warehouseProduct = {}

        for (k,v) in orderDetailsJson.items():
            if k in warehouse['inventory']:
                warehouseProductsize = warehouse['inventory'][k]
                if warehouseProductsize >= v and orderDetailsJson[k] != 0:
                    warehouseProduct[k] = v
                    orderDetailsJson[k] = 0
                elif orderDetailsJson[k] != 0:
                    warehouseProduct[k] = warehouseProductsize
                    orderDetailsJson[k] -= warehouseProductsize

        if len(warehouseProduct) > 0:
            tempresults.append({warehouse['name'] : warehouseProduct})

    for (k,v) in orderDetailsJson.items():
        if v != 0:
            for result in tempresults:
                for rkey in result:
                    del result[rkey][k] 

    for i in tempresults:
        for k in i:
            if len((i[k])) != 0:
                finalresults.append(i)
    
    return finalresults
