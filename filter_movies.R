install.packages("readr")
install.packages("dplyr")
library(readr)
library(dplyr)

#read in tsv
basics <- read_tsv("title.basics.tsv")
ratinfs <- read_tsv("title.ratings.tsv")

#merge and filter to include only movies
combined <- merge(basics, ratinfs, by="tconst")
movies <- filter(combined, titleType == 'movie')
#removed unnecessary columns
movies <- subset(movies, select = -c(originalTitle, isAdult, endYear))

#relevant movies have more than 1000 votes
movies <- filter(movies, numVotes > 1000)

write.csv(movies, "movies.csv", row.names = FALSE)
