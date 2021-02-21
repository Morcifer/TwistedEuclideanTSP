import os

from src.input_output.case_loader import CaseLoader
from src.input_output.solution_writer import SolutionWriter
from src.input_output.solution_plotter import SolutionPlotter

from src.algorithm.route_picker import RoutePicker

if __name__ == "__main__":
    folder = "data"
    input_file_name = "200_case.csv"
    output_file_name = "200_case_result.csv"

    vehicle_capacity = 800
    events = CaseLoader.load_case(os.path.join(folder, input_file_name))

    route_picker = RoutePicker(events, vehicle_capacity)
    solution_route = route_picker.find_best_route()

    SolutionWriter.write_solution(os.path.join(folder, output_file_name), solution_route.events)
    SolutionPlotter.plot_solution(events, solution_route.events)
