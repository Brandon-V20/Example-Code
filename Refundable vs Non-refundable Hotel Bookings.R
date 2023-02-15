install.packages("tidyverse")
library(tidyverse)

hotel <- read_csv("~/coursera csvs/hotel_bookings.csv")
View(hotel_bookings)

#install graphing packages

install.packages("ggplot2")
library(ggplot2)

#Bar Charts for channel distributions

ggplot(data=hotel) +
  geom_bar(mapping=aes(x=distribution_channel))

#fill use

ggplot(data=hotel) +
  geom_bar(mapping=aes(x=distribution_channel, fill=deposit_type))

#facet wrap

ggplot(data = hotel) +
  geom_bar(mapping = aes(x = distribution_channel,fill="red")) +
  facet_wrap(~deposit_type) +
  theme(axis.text.x = element_text(angle=45))

#facet grid

ggplot(data = hotel) +
  geom_bar(mapping = aes(x = distribution_channel,fill="red")) +
  facet_wrap(~deposit_type) +
  theme(axis.text.x = element_text(angle=45)) +
  labs(title="Refundable Hotel Bookings")


