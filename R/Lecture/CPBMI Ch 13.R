library(multtest)
data(golub, package="multtest")
?multtest::golub
View(golub)
View(golub.gnames)
head(golub.gnames)
golub.cl
which(golub.gnames[,2] == "CCND3 Cyclin D3")
gol.true <- factor(golub.cl, levels = 0:1, labels = c("ALL", "notALL"))
gol.pred <- factor(golub[1042, ] > 1.27, levels = c("TRUE","FALSE"))
table (gol.pred, gol.true)
boxplot(golub[1042, ]~ gol.true)
golub[1042,] 
range(golub[1042,])

gol.pred <- factor(golub[1042, ]>2.7, levels = c("TRUE","FALSE"))
table(gol.pred, gol.true)

gol.pred <- factor(golub[1042, ]>1.52, levels = c("TRUE","FALSE"))
table(gol.pred, gol.true)

# Create ROC curve, obtain AUC value
install.packages("ROCR")
library(ROCR)
gol.true <- factor(golub.cl, levels=0:1, labels = c("TRUE", "FALSE"))
pred <- prediction(golub[1042,], gol.true)
perf <- performance(pred, "tpr", "fpr")
plot(perf)
perf.auc <- performance(pred, "auc")@y.values[[1]]
perf.auc

# rpart classification package example - geneA single gene
set.seed(123)
n <- 10
sigma <- 0.5
fac <- factor(c(rep(1,n), rep(2,n), rep(3,n)))
levels (fac) <- c("ALL1", "ALL2", "ALL3")
geneA <- c(rnorm(10,0,sigma), rnorm(10,2, sigma), rnorm(10,4, sigma))
boxplot(geneA ~ fac)
dat <- data.frame(fac, geneA)

library(rpart)
rp <- rpart(fac~geneA, method="class", data=dat)
plot(rp, branch=0, margin=0.1)
text(rp, digits=3, use.n = TRUE)

# rpart classification using geneA + geneB + geneC
set.seed(123)
n <- 10
sigma <- 0.5
fac <- factor(c(rep(1,n), rep(2,n), rep(3,n)))
levels (fac) <- c("ALL1", "ALL2", "ALL3")
geneA <- c(rnorm(20,0,sigma), rnorm(10,2,sigma))
geneB <- c(rnorm(10,0,sigma), rnorm(20,2,sigma))
geneC <- c(rnorm(30,1,sigma))
dat <- data.frame(fac, geneA, geneB, geneC)
rp <- rpart(fac ~ geneA + geneB + geneC, method = "class", data=dat)
plot(rp, branch=0, margin=0.1)
text(rp, digits=3, use.n= TRUE)

# rpart example, golub dataset
gol.fac <- factor(golub.cl, levels=0:1, labels=c("ALL", "AML"))
gol.rp <- rpart(gol.fac ~ golub[1042,], method = "class")
plot(gol.rp, branch=0, margin=0.1)
text(gol.rp, digits=3, use.n = TRUE)
predictedclass <- predict(gol.rp, type="class")
table(predictedclass, gol.fac)

row.names(golub) <- paste("gene", 1:3051, sep="")
goldata <- data.frame(t(golub[1:3051,]))
gol.fac <- factor(golub.cl, levels = 0:1, labels = c("ALL", "AML"))
gol.rp <- rpart(gol.fac~., data=goldata, method="class", cp=0.001)
plot(gol.rp, branch=0, margin=0.1)
text(gol.rp, digits=3, use.n = TRUE)
golub.gnames[896,]

# Gene Selection
library(hgu95av2.db)
library(ALL)
data(ALL)
?ALL
ALLB123 <- ALL[, ALL$BT %in% c("B1","B2","B3")]
pano <- apply(exprs(ALLB123), 1, function(x) anova(lm(x~ALLB123$BT))$Pr[1])
names <- featureNames(ALL)[pano < 0.000001]
symb <- mget (names, env=hgu95av2SYMBOL)
ALLBTnames <- ALLB123[names,]
probedat <- as.matrix(exprs(ALLBTnames))
row.names(probedat) <- unlist(symb)

diagnosed <- factor(ALLBTnames$BT)
tr <- rpart(factor(ALLBTnames$BT)~., data=data.frame(t(probedat)))
plot(tr, branch=0, margin=0.1)
text(tr, digits =3, use.n = TRUE)
rpartpred <- predict(tr, type="class")
table(rpartpred, diagnosed)

# SVM
library(e1071)
df <- data.frame(Y=factor(ALLBTnames$BT), X=t(probedat))
Y <- factor(ALLBTnames$BT)
X <- t(probedat)
svmest <- svm(X,Y, data=df, type="C-classification", kernal="linear")
svmpred <- predict(svmest, X, probabilities=TRUE)
table(svmpred, factor(ALLBTnames$BT))
