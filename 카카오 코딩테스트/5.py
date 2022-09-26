def solution(commands):
    table = [["EMPTY"]*50 for _ in range(50)]
    answer = []
    MERGED = []
    for command in commands:
        cmd = list(command.split())
        cmd_type = cmd[0]
        if cmd_type == "UPDATE":
            if len(cmd) == 4:
                r = int(cmd[1]) - 1
                c = int(cmd[2]) - 1
                value = cmd[3]
                table[r][c] = value
            else:
                value1 = cmd[1]
                value2 = cmd[2]
                for i in range(50):
                    for j in range(50):
                        if table[i][j] == value1:
                            table[i][j] = value2
        if cmd_type == "MERGE":
            r1 = int(cmd[1])-1
            c1 = int(cmd[2])-1
            r2 = int(cmd[3])-1
            c2 = int(cmd[4])-1
            for lst in MERGED:
                for r, c in lst:
                    if r1 == r and c1 == c:
                        lst.append((r2, c2))
                        break
                    elif r2 == r and c2 == c:
                        lst.append((r1, c1))
                        break
            else:
                MERGED.append([(r1, c1), (r2, c2)])
            if table[r1][c1] == "EMPTY":
                table[r1][c1] = table[r2][c2]
            else:
                table[r2][c2] = table[r1][c1]
        if cmd_type == "UNMERGE":
            r1 = int(cmd[1])-1
            c1 = int(cmd[2])-1
            for lst in MERGED:
                for r, c in lst:
                    if r1 == r and c1 == c:
                        for x, y in lst:
                            if r1 == x and c1 == y:
                                continue
                            else:
                                table[x][y] = "EMPTY"
        if cmd_type == "PRINT":
            r, c = map(int, cmd[1:])
            answer.append(table[r-1][c-1])

    return answer