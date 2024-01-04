module Main where


import System.IO
import Control.Monad
import Data.Char
import Data.List.Split (splitOn)


trim :: String -> String
trim = f . f
   where f = reverse . dropWhile isSpace


limit :: String -> Int
limit "red"   = 12
limit "green" = 13
limit "blue"  = 14


possible :: String -> Bool
possible s = all (valid . map (words . trim) . splitOn ",") $ splitOn ";" $ unwords $ tail $ tail $ words s
    where valid = all valid'
          valid' [n, color] = read n <= limit color


getID :: String -> Int
getID s = getNum $ words s
    where getNum (_:n:_) = read $ init n


part1 :: [String] -> Int
part1 ln = sum $ map possibleID ln
    where possibleID l | possible l = getID l
                       | otherwise  = 0


getMax :: (Int, Int, Int) -> [[String]] -> (Int, Int, Int)
getMax (r, g, b) [] = (r, g, b)
getMax (r, g, b) ([n,color]:xs) | color == "red"   = getMax (max (read n) r, g, b) xs
                                | color == "green" = getMax (r, max (read n) g, b) xs
                                | color == "blue"  = getMax (r, g, max (read n) b) xs


part2 :: [String] -> Int
part2 ln = sum $ map (power . getMax (1, 1, 1) . parse) ln
    where parse l = concatMap (map (words . trim) . splitOn ",") $ splitOn ";" $ unwords $ tail $ tail $ words l
          power (a, b, c) = a * b * c


main :: IO ()
main = do
    handle <- openFile "input02.txt" ReadMode
    content <- hGetContents handle
    putStrLn $ "Part 1: " ++ (show . part1 . lines $ content)
    putStrLn $ "Part 2: " ++ (show . part2 . lines $ content) 
