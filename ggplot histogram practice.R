install.packages("ggplot2")
library(ggplot2)
install.packages("palmerpenguins")
library(palmerpenguins)

data(penguins)
View(penguins)


ggplot(penguins, aes(x=flipper_length_mm)) + geom_histogram(aes(y=..density..), color="pink", fill="white") + geom_density(alpha=.7, fill="#FF8321")
