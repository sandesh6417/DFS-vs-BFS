# AI Contribution Log

**Project:** 8-Puzzle BFS vs DFS Profiling  
**Course:** 02AML204 – Introduction to Artificial Intelligence  
**PRN:** 25UAM044  
**Name:** SANDESH PATIL  

## 1. AI Tool Used

**AI Tool:** Claude (Anthropic)

AI assistance was used during the development and documentation of the BFS and DFS 8-puzzle profiling project.

## 2. Contribution Details

| Sr. No. | Task | AI Contribution | My Contribution |
|---|---|---|---|
| 1 | Problem setup | Helped structure the 8-puzzle problem using BFS and DFS. | Selected the start and goal states. |
| 2 | BFS implementation | Assisted in writing the initial BFS implementation using a queue, visited set, and parent tracking. | Reviewed and understood the BFS logic. |
| 3 | DFS implementation | Assisted in writing the iterative DFS implementation using a stack, visited set, parent tracking, and depth limit. | Reviewed and understood the DFS logic. |
| 4 | Neighbor generation | Assisted with the `neighbors()` function for generating valid puzzle moves. | Verified that the generated moves were appropriate for the 8-puzzle. |
| 5 | Node counting | Helped include the `nodes_expanded` counter. | Used the counter to understand the search effort of BFS and DFS. |
| 6 | Execution-time measurement | Assisted with timing the algorithms using `time.perf_counter()`. | Ran the program and reviewed the timing results. |
| 7 | Multiple trials | Helped structure three runs and calculate average execution time. | Used the three-run results in the profiling analysis. |
| 8 | cProfile analysis | Assisted with using Python profiling to examine function-level execution. | Reviewed the profiling results and interpreted the major differences. |
| 9 | Results analysis | Helped organize the comparison between BFS and DFS. | Verified the results against BFS/DFS theory. |
| 10 | Report writing | Assisted with the structure and wording of the profiling report. | Prepared the final report and analysis. |
| 11 | README | Assisted in preparing the GitHub README structure. | Reviewed the content and used it for the project repository. |
| 12 | Flame graph | Assisted with profiling visualization. | Reviewed the generated flame graph and its relationship to the program. |

## 3. Code Areas Assisted by AI

AI assistance was mainly used for:

- `neighbors(state)` — generation of possible puzzle states.
- `bfs(start)` — Breadth-First Search implementation.
- `dfs(start, max_depth=30)` — depth-limited iterative Depth-First Search.
- `run_trials(fn, runs=3)` — repeated execution and average timing.
- `nodes_expanded` — counting processed states.
- `parent` dictionary — reconstructing the solution path.
- Timing using `time.perf_counter()`.

## 4. Human Verification

The AI-generated code was reviewed rather than used blindly. I:

1. Reviewed the BFS and DFS logic.
2. Understood how the queue and stack work.
3. Selected and checked the 8-puzzle start and goal states.
4. Verified the number of nodes expanded.
5. Checked the solution path lengths.
6. Compared the measured results with BFS and DFS theory.
7. Prepared the final analysis and conclusion.
8. Reviewed the final project files before submission.

## 5. Final Results Used

The final profiling report recorded:

- **BFS:** 0.017 ms average time, 3 nodes expanded, 2-move solution.
- **DFS:** 19.38 ms average time, 17,742 nodes expanded, 22-move solution.
- DFS was approximately **1,140× slower** in the reported experiment.

These results were used to demonstrate the practical difference between BFS and DFS on the selected 8-puzzle problem.

## 6. Declaration

AI was used as an assistance tool for coding, profiling support, visualization, and documentation. I reviewed the generated material, understood the algorithmic logic, verified the results, and prepared the final project submission.
