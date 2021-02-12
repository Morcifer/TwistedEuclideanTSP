from src.input_output.case_loader import CaseLoader
from src.input_output.solution_writer import SolutionWriter
from src.input_output.solution_plotter import SolutionPlotter

if __name__ == "__main__":
    events = CaseLoader.load_case("data/200_case.csv")
    print(events)
    SolutionWriter.write_solution("data/200_case_result.csv", events)
    SolutionPlotter.plot_solution(events, events)
