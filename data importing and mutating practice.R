head(hotel_bookings)
bookings_df  <- data(hotel_bookings)

bookings_df <- read_csv("hotel_bookings.csv")
library(readr)
bookings_df <- read_csv("Coursera data analysis course/hotel_bookings.csv")
View(bookings_df)

new_df <-select(bookings_df, 'adr', adults)
library(tidyverse)
View(new_df)

mutate(new_df, total = 'adr' / adults)
