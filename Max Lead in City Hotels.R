install.packages("tidyverse")
install.packages("skimr")
install.packages("janitor")

library(tidyverse)
library(skimr)
library(janitor)

library(readr)
hotel_bookings <- read_csv("~/Coursera csvs/hotel_bookings.csv")
view(hotel_bookings)


hotel_bookings_v2 <- arrange(hotel_bookings, desc(lead_time))
view(hotel_bookings_v2)

max(hotel_bookings_v2$lead_time)

city_hotels <- filter(hotel_bookings, hotel_bookings$hotel=="City Hotel")
View(city_hotels)

mean(city_hotels$lead_time)

penguins %>% 
  
  drop_na() %>% 
  
  group_by(species) %>%

  summarize(max_flipper = max(flipper_length_mm))

view(penguins)




