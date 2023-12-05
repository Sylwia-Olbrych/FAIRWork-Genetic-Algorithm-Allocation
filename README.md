Developers: [Zi Xuan(Melody) Tung](https://github.com/melody-tung), [Alexander Nasuta](https://github.com/Alexander-Nasuta)
 Sylwia Olbrych

“This work has been supported by the FAIRWork project (www.fairwork-project.eu) and has been funded within the European Commission’s Horizon Europe Programme under contract number 101049499. This paper expresses the opinions of the authors and not necessarily those of the European Commission. The European Commission is not liable for any use that may be made of the information contained in this presentation.”

This project provides genetic algorithm to calculate the best worker to order combination by considering worker preference and central allocation of workers. 


***
# Resource Allocation - Genetic Algorithm

This Python code implements a genetic algorithm for resource allocation, focusing on worker-order assignments based on worker preferences and central allocation. The code is designed to find an optimal assignment that maximizes a score, which can represent efficiency, cost-effectiveness, or other relevant factors.

## Key Components
- `dummy_data.py`: This file generates dummy data in place of real data that can be input into the algorithm. 

- `genetic_algorithm.py`: This file contains the core logic for the genetic algorithm, including initialization, scoring, selection, crossover, elitist update, mutation, and finding the best solution.

- `read_data.py`: This file reads input data from an Excel file and extracts worker preferences and machine preferences for different orders. You can adjust the Excel file path, sheet names, and column ranges to suit your specific data structure.

- `validation.py`: This file serves as a validation tool to ensure the effectiveness of the genetic algorithm by providing the execution time if all the scores of possible worker-to-order combinations are calculated. It generates and evaluates permutations for all possible worker-to-order combinations. It calculates scores for each permutation and identifies the one with the highest score as the best worker-to-order combination. The execution time is also measured, and the resulting output is then compared to the genetic algorithm's results. *Note that the computation time could take a very long time to run this if the number of permutations gets too large because of the factorial growth of possibilities, resulting in an exponential increase in the time complexity. 

- `main.py`: This file is the main script that executes the algorithm. Defines parameters such as population size, crossover and mutation probabilities, and stopping criteria. Utilizes the genetic algorithm functions for resource allocation and displays results, including a graphical representation of score evolution over generations.

## Usage

1. Ensure you have Python 3.11 installed.

2. Make sure to have the required libraries, such as matplotlib, NumPy and Pandas, installed. The required libraries are specified in the `requirements.txt` file.

3. A dummy set of data is provided but if there is a need to input own data into the algorithm, modify the data source in `read_data.py` by providing the path to your Excel file and adjusting the data reading settings to match your dataset. You should provide the following information:

   - `excel_file`: Define the path to your Excel file, including the file name and extension.
   - `sheet_names`: Define the names of the Excel sheets that contain the relevant data.
   - `start_rows`: Specify the starting rows for each order's data in the Excel sheets.
   - `worker_columns`: Define the range of columns to read for worker preferences.
   - `central_data_columns`: Define the range of columns to read for resilience data.

4. Once you've customized the data source settings in `read_data.py` or decided to use the dummy_data, the genetic algorithm code will use the provided Excel file or dummy datd to extract worker preferences and machine preferences for resource allocation.

5. Make sure that the Excel file format and data structure match the expectations of the code for proper execution.

6. You can now calculate the best worker to order allocation. 

## Additional Customization

7. Depending on your specific use case, you may want to adjust other parameters in the genetic algorithm code, such as the probabilities of crossover (`Pc`) and mutation (`Pm`), the number of generations (`stopGeneration`), and any constraints or objectives specific to your resource allocation problem.
Parameters (Pc and Pm)

In the genetic algorithm, two critical parameters control the probabilistic operations of crossover and mutation, which are key to the algorithm's success:

- `Pc` - Crossover Probability:
  - Crossover, also known as recombination, is a genetic operation where two parent individuals combine their genetic material to create one or more offspring individuals. This operation introduces diversity into the population and allows for the exchange of genetic information between parents.
  - `Pc` is the probability of applying crossover to a pair of parent individuals during the creation of the next generation. It controls how often crossover occurs.
  - A value of `Pc` between 0 and 1 represents the likelihood of crossover occurring. For example:
    - `Pc = 0.7` means there's a 70% chance of crossover happening.
    - `Pc = 0.2` means there's a 20% chance of crossover happening.
  - The choice of `Pc` affects the balance between exploration and exploitation in the genetic algorithm. Higher values promote exploration by encouraging more frequent recombination of genetic material, while lower values promote exploitation by reducing the occurrence of crossover.

- `Pm` - Mutation Probability:
  - Mutation is a genetic operation that introduces random changes to individual chromosomes. It helps maintain diversity in the population and can potentially lead to the discovery of new, better solutions.
  - `Pm` is the probability of applying mutation to an individual's chromosome during the creation of the next generation. It controls how often mutation occurs.
  - Similar to `Pc`, `Pm` is represented as a probability value between 0 and 1, where:
    - `Pm = 0.1` means there's a 10% chance of mutation happening.
    - `Pm = 0.5` means there's a 50% chance of mutation happening.
  - The choice of `Pm` is crucial for introducing exploration and diversity within the population. A lower value of `Pm` results in fewer mutations and potentially slower exploration of the solution space, while a higher value may lead to more rapid exploration.

When using the genetic algorithm, you should adjust Pc and Pm based on your specific problem and dataset. The best values for these parameters can differ between problems, so it's important to experiment to find the right balance.
Additionally, the `validation.py` script serves as a valuable tool for objectively validating the performance of the genetic algorithm. This includes assessing its efficiency in comparison to a heuristic approach, wherein all possible combinations are exhaustively calculated. Such a comprehensive validation process ensures the robustness and efficacy of the genetic algorithm in resource allocation scenarios.
***
“This work has been supported by the FAIRWork project (www.fairwork-project.eu) and has been funded within the European Commission’s Horizon Europe Programme under contract number 101049499. This paper expresses the opinions of the authors and not necessarily those of the European Commission. The European Commission is not liable for any use that may be made of the information contained in this presentation.”

Copyright © RWTH of FAIRWork Consortium
