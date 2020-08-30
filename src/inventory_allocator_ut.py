import unittest
import inventory_allocator as ia

class TestInventoryAllocator(unittest.TestCase):
    
# Test Case 1 returns the cheapest shipment where orders are shipped from one wwarehouse

    def test_case_one(self):
        orderDetails = "{\"strawberry\":1}"
        warehouseDetails = "[{\"name\":\"owd\",\"inventory\":{\"strawberry\":1}}]"        
        expectedresult = "[{'owd': {'strawberry': 1}}]"
        actualtresult = ia.allocate(orderDetails, warehouseDetails)
        self.assertEqual(expectedresult, str(actualtresult))
        
# Test case 2 shows 2 orders can be shipped from multiple warehouses

    def test_case_two(self):
        orderDetails = "{\"strawberry\":2,\"blueberry\":6}"
        warehouseDetails = "[{\"name\":\"owd\",\"inventory\":{\"strawberry\":5,\"blueberry\":5}},{\"name\":\"dm\",\"inventory\":{\"blueberry\":5,\"orange\":10,\"strawberry\":10}}]"
        expectedresult = "[{'owd': {'strawberry': 2, 'blueberry': 5}}, {'dm': {'blueberry': 1}}]"
        actualtresult = ia.allocate(orderDetails, warehouseDetails)
        self.assertEqual(expectedresult, str(actualtresult))
        
# Test case 3 returns that there's no enough inventory 

    def test_case_three(self):
        orderDetails = "{\"strawberry\":2,\"blueberry\":1}"
        warehouseDetails = "[{\"name\":\"owd\",\"inventory\":{\"strawberry\":1,\"blueberry\":0}}]"
        expectedresult = "[]"
        actualtresult = ia.allocate(orderDetails, warehouseDetails)
        self.assertEqual(expectedresult, str(actualtresult))
   
# Test case 4 shows that there's no enough inventory 

    def test_case_four(self):
        orderDetails = "{\"blueberry\":1}"
        warehouseDetails = "[{\"name\":\"owd\",\"inventory\":{\"blueberry\":0}}]"
        expectedresult = "[]"
        actualtresult = ia.allocate(orderDetails, warehouseDetails)
        self.assertEqual(expectedresult, str(actualtresult))

# Test case 5 produces empty as warehouse details are not given

    def test_case_five(self):
        orderDetails = "{\"strawberry\":10}"
        warehouseDetails = "[]"
        expectedresult = "[]"
        actualtresult = ia.allocate(orderDetails, warehouseDetails)
        self.assertEqual(expectedresult, str(actualtresult))
        
        
# Test case 6 shows order can be shipped from multiple warehouses
         
    def test_case_six(self):
        orderDetails = "{\"strawberry\":10}"
        warehouseDetails = "[{\"name\":\"owd\",\"inventory\":{\"strawberry\":5}},{\"name\":\"dm\",\"inventory\":{\"strawberry\":5}}]"
        expectedresult = "[{'owd': {'strawberry': 5}}, {'dm': {'strawberry': 5}}]"
        actualtresult = ia.allocate(orderDetails, warehouseDetails)
        self.assertEqual(expectedresult, str(actualtresult))
        
  
if __name__ == '__main__':
    unittest.main()


