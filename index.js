const text = `
   MON
   TOR
   2     BOS
   3     NYR
   4     CHI
   5     DET
   6      LA
   7     DAL
   8     PHI
   9     PIT
   10    STL
   11    BUF
   12    VAN
   13    CAL
   14    NYI
   15     NJ
   16    WAS
   17    EDM
   18    CAR
   19    COL
   20    ARI
   21     SJ
   22    OTT
   23     TB
   24    ANA
   25    FLA
   26    NAS
   27    WIN
   28    CLB
   29    MIN
   30    VEG
`;

// Split the text into lines
const lines = text.trim().split('\n');

// Filter and map the lines to create an array of team names
const teamNames = lines.filter(line => !/^\d+\s+/.test(line)).map(line => line.trim());
console.log(teamNames)