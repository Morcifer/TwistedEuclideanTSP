from src.input_output.case_loader import CaseLoader
from src.input_output.solution_writer import SolutionWriter
from src.input_output.solution_plotter import SolutionPlotter

from src.algorithm.route_picker import RoutePicker

if __name__ == "__main__":
    vehicle_capacity = 200
    events = CaseLoader.load_case("data/200_case.csv")

    route_picker = RoutePicker(events, vehicle_capacity)
    solution_route = route_picker.find_best_route()

    SolutionWriter.write_solution("data/200_case_result.csv", solution_route.events)
    SolutionPlotter.plot_solution(events, solution_route.events)
