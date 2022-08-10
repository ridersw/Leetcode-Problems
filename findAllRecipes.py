class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        result = []
        
        for swi in range(len(recipes)):
            print(f'for recipe: {recipes[swi]}')
            


if __name__ == "__main__":
    obj = Solution()

    recipes = ["bread","sandwich"]
    ingredients = [["yeast","flour"],["bread","meat"]]
    supplies = ["yeast","flour","meat"]

    print(obj.findAllRecipes(recipes, ingredients, supplies))


                