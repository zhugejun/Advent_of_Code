
# perfect ticyverse solution from @drob
# https://twitter.com/drob/status/1730817227371225487

library(tidyverse)

# have to load d first

d = read_lines("2023/input2.txt") |>
    as_tibble() |>
    rename(x = value)

game_cubes = d |>
    mutate(game = row_number()) |>
    mutate(cubes = str_extract_all(x, "\\d+ [a-z]+")) |>
    unnest(cubes) |>
    separate(cubes, c("number", "color"), sep = " ", convert = TRUE)


# part 1

maxima = c(red = 12, green = 13, blue = 14)

game_cubes |>
    mutate(maximum = maxima[color]) |>
    group_by(game) |>
    summarise(playable = !any(number > maximum)) |>
    filter(playable) |>
    summarise(sum(game))


# part 2

game_cubes |>
    group_by(game, color) |>
    summarise(number = max(number)) |>
    summarise(power = prod(number)) |>
    summarise(sum(power))
