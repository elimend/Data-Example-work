library(tidyverse)

# Load data
df <- read.csv("health_data.csv", stringsAsFactors = FALSE)

# Data preprocessing
df$date <- lubridate::mdy(df$date)
df$age <- as.integer(df$age)
df <- df %>% na.omit(select = c("weight", "height"))

# Feature engineering
df$bmi <- df$weight / (df$height / 100) ^ 2
df$risk <- ifelse(df$bmi >= 25, "High", "Low")

# Data visualization
ggplot(df, aes(x = bmi, fill = risk)) +
  geom_histogram(alpha = 0.7, bins = 30) +
  ggtitle("Distribution of BMI by Risk Level") +
  xlab("BMI") +
  ylab("Count")

# Data analysis
avg_bmi <- mean(df$bmi, na.rm = TRUE)
std_bmi <- sd(df$bmi, na.rm = TRUE)
max_bmi <- max(df$bmi, na.rm = TRUE)

cat("Average BMI:", round(avg_bmi, 2), "\n")
cat("Standard deviation of BMI:", round(std_bmi, 2), "\n")
cat("Maximum BMI:", round(max_bmi, 2), "\n")
