
input_file = 'input.txt'
output_file = 'output.txt'

begin
  content = File.read(input_file)
  modified_content = content.upcase 

  File.open(output_file, 'w') do |file|
    file.write(modified_content)
  end
  puts "File processing complete. Output written to #{output_file}"
rescue => e
  puts "Error: #{e.message}"
end
