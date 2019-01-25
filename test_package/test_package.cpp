// #include <cpprest/json.h>
#include <toml/toml.h>
#include <ifstream>
#include <iostream>

int main()
{
  std::ifstream ifs("foo.toml");
  toml::ParseResult pr = toml::parse(ifs);

  if (!pr.valid()) {
    std::cout << pr.errorReason << std::endl;
    return;
  }
}
