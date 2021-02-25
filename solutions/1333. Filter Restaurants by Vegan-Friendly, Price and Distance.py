class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        if veganFriendly:
            restaurants = list(filter(lambda x: x[2],restaurants))
        
        restaurants = list(filter(lambda x:x[3]<=maxPrice and x[4]<=maxDistance,restaurants))
        restaurants.sort(key=lambda x:(-x[1],-x[0]))
        restaurants = list(map(lambda x: x[0],restaurants))
        return restaurants
        
