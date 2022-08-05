class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        result = []
        
        for swi in range(len(recipes)):
            print(f'Recipe: {recipes[swi]} needs Ingredients: {ingredients[swi]} Are Ingredients in Supplies: {ingredients[swi] in supplies}')

if __name__ == "__main__":
    obj = Solution()

    recipes = ["bread","sandwich"]
    ingredients = [["yeast","flour"],["bread","meat"]]
    supplies = ["yeast","flour","meat"]

    print(obj.findAllRecipes(recipes, ingredients, supplies))


                