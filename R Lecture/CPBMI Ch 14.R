# Survival Analysis
library(survival)
library(ISwR)
head(melanom)
attach(melanom)

# Create Surv Object
Surv(days, status == 1)  # Surv(time, event)
head(Surv(days, status==1))

# Kaplna-Meier estimator
surv.bysex <- survfit(Surv(days, status == 1)~sex)
summary(surv.bysex)
plot(surv.bysex)
plot(surv.bysex, conf.int=TRUE, col=c("red", "blue"))

# Log - Rank test
survdiff(Surv(days, status == 1)~sex)

# Stratified analysis = strata(...), cluster(...)
survdiff(Surv(days, status==1)~sex + strata(ulc))  

# Cox proportional hazard model
summary(coxph(Surv(days, status == 1) ~ sex))
summary(coxph(Surv(days, status == 1) ~ sex + log(thick) + strata(ulc)))

# Survival ovarian cancer under monotherapy or combined
detach(melanom)

mydata <- read.csv("http://cpbmi.or.kr/ovarian.csv")
attach(mydata)
head(mydata)

mysurv <- Surv(time, status == 1)
myKMtest <- survfit(mysurv ~ group, conf.int=FALSE)

plot(myKMtest, lty=c(1,3), col=c("blue", "red"))
title (main = "Survival ovarian cancer n=26", 
       xlab="Time (days)", ylab = "% surviving, S(t)")
legend(x=10, y=0.25, legend = c("monotherapy", "combined"), 
       col=c("blue", "red"), lty=c(1,1))
summary(myKMtest)

my_coxph_full <- coxph(mysurv ~ group + age, mydata)
summary(my_coxph_full)

my_coxph_reduced <- coxph(mysurv ~ age, mydata)
summary(my_coxph_reduced)

## testing deviance
anova(my_coxph_full, my_coxph_reduced, test="Chisq")
