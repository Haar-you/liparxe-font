#!/usr/bin/ruby


require "rexml/document"
require "builder"

svg = REXML::Document.new(open("liparxe.svg"))

glyphs = %w[p fh f t c x k q h r z m n l j w b vh v d s g dz long_r i y u o e a 0 1 2 3 4 5 6 7 8 9 period comma excl ques apos quot]

svg.elements.each("svg/g/path") do |elem|
  id = elem.attributes["id"]
  d = elem.attributes["d"]

  m = d.scan(/[\-\d\.]+/)
  dx = m[0].to_i
  dy = 1052.3622 - m[1].to_i


  if glyphs.include?(id) then
    File.open("glyphs/#{id}.svg", "w") do |file|
      xml = Builder::XmlMarkup.new(:indent=>2, :target=>file)
      xml.instruct!(:xml, :version=>"1.0", :encoding=>"UTF-8")
      xml.svg(
        :'xmlns:svg'=>"http://www.w3.org/2000/svg",
        :xmlns=>"http://www.w3.org/2000/svg",
        :viewBox=>"0 0 1000 1000"){

        xml.path(
          :transform=>"translate(#{-(dx/1000).to_i*1000},0)",
          :style=>"fill:#000000;fill-opacity:1;stroke:none",
          :d=>d
        )
      }
    end
  end
  
end

