names <- c("Peter", "Jennifer", "Julie", "Alex")
age <-c(15, 19, 21, 25)

people <-data.frame(names, age)
View(people)
head(people)
colnames(people)

mutate(people, age_in_20 = age + 20)
View(mutate(people))
as_tibble(diamonds)

