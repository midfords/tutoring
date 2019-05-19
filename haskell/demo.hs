
-- Basic Functions
doubleMe x = x * x
doubleUs x y  = x * 2 + y * 2
doubleSmall' x = if x > 5 then x else doubleMe x
concatList x y = x ++ y
elementAt x y = x !! y

-- List Comprehension
lengthOdd st = sum [1 | a <- st, odd a]

-- Lists
list = 1:2:3:[]
list2 = [1,2,3]

-- Function Definitions
factorial :: Integer -> Integer
factorial n = product [1..n]
isPrimeNumber :: Integer -> Bool
isPrimeNumber n = [s | s <- [2..n-1], n `rem` s == 0] == []

-- Recursion
maximum' :: (Ord a) => [a] -> a
maximum' [] = error "Maximum of empty list."
maximum' [x] = x
maximum' (x:xs)
    | x > maxTail = x
    | otherwise = maxTail
    where maxTail = maximum' xs

-- Lambdas (GHCI example)
-- zipWith (\a b -> (a * 30 + 3) / b) [5,4,3,2,1] [1,2,3,4,5]

-- Simplifying functions with function composition(.) and function application ($)
oddSquareSum1 :: Integer
oddSquareSum1 = sum (takeWhile (<10000) (filter odd (map (^2) [1..])))

oddSquareSum2 :: Integer
oddSquareSum2 = 
    let oddSquares = filter odd $ map (^2) [1..]
        belowLimit = takeWhile (<10000) oddSquares
    in sum belowLimit

oddSquareSum3 :: Integer
oddSquareSum3 = sum . takeWhile (<10000) . filter odd . map (^2) $ [1..]
