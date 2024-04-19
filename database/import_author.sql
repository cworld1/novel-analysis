CREATE TABLE IF NOT EXISTS author_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- 这里添加了一个自增的主键字段
    BookId BIGINT,
    Name VARCHAR(255),
    TotalWorks VARCHAR(255),
    TotalWords VARCHAR(255),
    TotalDays VARCHAR(255),
    LevelTag VARCHAR(255),
    ImgLink VARCHAR(255),
    Books TEXT
);
TRUNCATE TABLE novels;
LOAD DATA INFILE 'E:/ProgramsHW/shixi/novel_analysis/data/authors.csv' INTO TABLE novels FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES (
    BookId,
    Name,
    Author,
    Type,
    IsCompleted,
    Popularity,
    @Intro
)
SET Intro = REPLACE(@Intro, '\\n', '\n');
CREATE TABLE IF NOT EXISTS novels (
    BookId BIGINT PRIMARY KEY,
    Name VARCHAR(255),
    Author VARCHAR(255),
    Type VARCHAR(255),
    IsCompleted VARCHAR(255),
    Popularity VARCHAR(255),
    Intro LONGTEXT
);
TRUNCATE TABLE novels;
LOAD DATA INFILE 'E:/ProgramsHW/shixi/novel_analysis/data/books.csv' INTO TABLE novels FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES (
    BookId,
    Name,
    Author,
    Type,
    IsCompleted,
    Popularity,
    @Intro
)
SET Intro = REPLACE(@Intro, '\\n', '\n');
CREATE TABLE IF NOT EXISTS rankings (
    Category VARCHAR(255),
    `Rank` INT,
    Title VARCHAR(255),
    BookId BIGINT,
    Link VARCHAR(255),
    PRIMARY KEY (Category, `Rank`)
);
LOAD DATA INFILE 'E:/ProgramsHW/shixi/novel_analysis/data/ranking.csv' INTO TABLE rankings FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES (Category, `Rank`, Title, BookId, Link);