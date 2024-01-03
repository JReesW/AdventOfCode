module Main where


import System.IO
import Control.Monad
import Data.Char
import Data.Text (replace, pack, unpack)
import Data.List (elemIndex, isInfixOf)
import Data.Maybe


names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


replaceName :: String -> String -> String
replaceName target name | name `isInfixOf` target = packed name (name ++ show (fromJust (elemIndex name names) + 1) ++ name) target
                        | otherwise               = target
    where packed :: String -> String -> String -> String
          packed n w = unpack . replace (pack n) (pack w) . pack


first :: [Char] -> Int
first (c:cs) | isDigit c = digitToInt c
             | otherwise = first cs


firstAndLast :: String -> Int
firstAndLast s = (first s * 10) + first (reverse s)


part1 :: [String] -> Int
part1 ln = sum $ map firstAndLast ln


part2 :: [String] -> Int
part2 ln = sum $ map f ln
    where f line = firstAndLast $ foldl replaceName line names


main :: IO ()
main = do
    handle <- openFile "input01.txt" ReadMode
    content <- hGetContents handle
    putStrLn $ "Part 1: " ++ (show . part1 . lines $ content)
    putStrLn $ "Part 2: " ++ (show . part2 . lines $ content) 
