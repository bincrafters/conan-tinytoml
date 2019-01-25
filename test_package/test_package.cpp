// #include <cpprest/json.h>
#include <toml/toml.h>

int main()
{
  std::ifstream ifs("foo.toml");
  toml::ParseResult pr = toml::parse(ifs);

  if (!pr.valid()) {
    cout << pr.errorReason << endl;
    return;
  }
}
