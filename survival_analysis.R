library(survival)
data <- read.table("kellydat.txt", header = TRUE)

dat.survival <- Surv(data$nctdel, data$fail)
km <- survfit(dat.survival ~ 1)
plot(km)
km2 <- survfit(dat.survival ~ data$black + data$hisp)
