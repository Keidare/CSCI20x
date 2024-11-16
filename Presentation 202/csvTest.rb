require 'csv'

input_file = 'data.csv'
output_file = 'filtered_data.csv'

def filter_csv(input_file, output_file, *columns)
  CSV.open(output_file, 'w') do |csv_out|
    CSV.foreach(input_file, headers: true) do |row|
      csv_out << columns.map { |col| row[col] }
    end
  end

  puts "Filtered data saved to #{output_file}"
end

filter_csv(input_file, output_file, 'Name', 'Email')
