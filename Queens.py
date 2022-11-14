# Counts the number of queens on the same row as the queen at index

def CountRow(index, buf):
    cmp = buf[index];
    count = 0;

    for i in range(0, 8):
        if(buf[i] == cmp):
            count = count + 1;

    return count;

# Counts the number of queens on the same left diagonal as the queen at index

def CountLeftDiagonal(index, buf):
    x = index;
    y = buf[index];
    count = 0;

    if(x < y):
        y = y - x;
        x = 0;

        while(y < 8):
            if(buf[x] == y):
                count = count + 1;

            x = x + 1;
            y = y + 1;
    else:
        x = x - y;
        y = 0;

        while(x < 8):
            if(buf[x] == y):
                count = count + 1;

            x = x + 1;
            y = y + 1;

    return count;

# Counts the number of queens on the same right diagonal as the queen at index

def CountRightDiagonal(index, buf):
    x = index;
    y = buf[index];
    count = 0;

    if((7 - x) < y):
        x = x - 7 + y;
        y = 7;

        while(x < 8):
            if(buf[x] == y):
                count = count + 1;

            x = x + 1;
            y = y - 1;
    else:
        y = y + x;
        x = 0;

        while(y >= 0):
            if(buf[x] == y):
                count = count + 1;

            x = x + 1;
            y = y - 1;

    return count;

# Checks to see if queens are attacking each other
# returns 8 if the queens are safe and less than 8 if not

def EightQueensAreSafe(buf):
    i = 0;
    count = 0;

    while(i < 8):
        if(CountRow(i, buf) == 1):
            if(CountLeftDiagonal(i, buf) == 1):
                if(CountRightDiagonal(i, buf) == 1):
                    count = count + 1;
        i = i + 1;

    return count;

# Increments the queens array by 1
# returns 1 if the increment overflows the array and 0 if it does not

def EightQueensStep(buf):
    i = 8;
    a = 0;
    b = 0;
    c = 1;

    while(i > 0):
        i = i - 1;
        a = buf[i];
        b = a + c;

        if(b > 7):
            b = 0;
            c = 1;
        else:
            c = 0;

        buf[i] = b;

    return c;

# Eight Queens main script
import sys

queens = [0,0,0,0,0,0,0,0];
solutions = 0;
out_file = "";

if(len(sys.argv) < 2):
    out_file = "out.txt";
else:
    if(sys.argv[1] != sys.argv[0]):
        out_file = sys.argv[1];
    else:
        print("Invalid output file name");
        exit();

if(len(out_file) == 0):
    print("Invalid output file name");
    exit();

f = open(out_file, "w");

print("PROCESSING");

while(1):
    if(EightQueensAreSafe(queens) == 8):
        f.write("A:{0} B:{1} C:{2} D:{3} E:{4} F:{5} G:{6} H:{7}\n".format(queens[0], queens[1], queens[2], queens[3], queens[4], queens[5], queens[6], queens[7]));
        solutions = solutions + 1;
  
    if(EightQueensStep(queens) == 1):
        break;

print("FINISHED");
print("{0}".format(solutions));


f.close();