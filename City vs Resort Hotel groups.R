hotel <- read.csv("~/coursera csvs/hotel_bookings.csv")
View(hotela)

#starting with point plot

ggplot(data=hotel) +
  geom_point(mapping=aes(x=lead_time, y= children))

#bar chart

ggplot(data=hotel) +
  geom_bar(mapping=aes(x=hotel, fill=market_segment))

#the many colors are the separate segments

#using facet_wrap

ggplot(data=hotel) +
  geom_bar(mapping=aes(x=hotel)) +
  facet_wrap(~market_segment)

#filtering for online ta city

onlineta_city_hotels <- filter(hotel, 
                               (hotel=="City Hotel" & 
                                  hotel$market_segment=="Online TA"))

#plotting on the filtered data

ggplot(data = onlineta_city_hotels) +
  geom_point(mapping=aes(x=lead_time, y=children))

View(onlineta_city_hotels)
