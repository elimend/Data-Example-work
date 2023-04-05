# Load data
customers <- read.csv("customer_data.csv")

# Data preprocessing
customers$date <- as.Date(customers$date)
customers$age <- as.integer(customers$age)
customers <- subset(customers, !is.na(gender) & !is.na(income))

# Feature engineering
customers$age_group <- cut(customers$age, breaks = c(0, 18, 25, 35, 50, 65, Inf),
                            labels = c("0-18", "19-25", "26-35", "36-50", "51-65", "66+"))
customers$age_income <- cut(customers$income, breaks = c(0, 30000, 50000, 75000, 100000, 150000, Inf),
                            labels = c("0-30k", "30k-50k", "50k-75k", "75k-100k", "100k-150k", "150k+"))

# Data visualization
library(ggplot2)
ggplot(customers, aes(x = age_group, fill = gender)) + geom_bar()

ggplot(customers, aes(x = age_income, y = balance)) + 
  stat_summary(fun = "mean", geom = "bar") +
  stat_summary(fun = "mean", geom = "errorbar", width = 0.2) +
  xlab("Age Income") + ylab("Balance")

# Data analysis
num_customers <- nrow(customers)
num_males <- sum(customers$gender == "Male")
num_females <- sum(customers$gender == "Female")
num_transactions <- sum(customers$transactions)
avg_balance <- mean(customers$balance)
std_balance <- sd(customers$balance)
