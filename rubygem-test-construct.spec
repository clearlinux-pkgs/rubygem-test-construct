#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-test-construct
Version  : 1.2.2
Release  : 7
URL      : https://rubygems.org/downloads/test-construct-1.2.2.gem
Source0  : https://rubygems.org/downloads/test-construct-1.2.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-metaclass
BuildRequires : rubygem-mocha
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
## THIS GEM IS DEPRECATED
The successor RubyGem (with a more consistent gem name) is [TestConstruct](https://github.com/bhb/test_construct). Please report all issues there.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n test-construct-1.2.2
gem spec %{SOURCE0} -l --ruby > rubygem-test-construct.gemspec

%build
gem build rubygem-test-construct.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
test-construct-1.2.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/test-construct-1.2.2
ruby -v -I.:lib:test test*/test_*.rb
ruby -v -I.:lib:test test*/*_test.rb || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/test-construct-1.2.2.gem
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/.devver/hooks/build
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/.devver/hooks/install_dependencies
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/.devver/hooks/notify
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/.devver/hooks/prepare_database
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/History.txt
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/README.markdown
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/bugs/issue-0127c8c6ba1d31b5488f4551f8d869e57d53956d.yaml
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/bugs/issue-404e5da7b128e5b34e7a33fbcd56603618010d92.yaml
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/bugs/issue-50798912193be32b1dc610d949a557b3860d96fd.yaml
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/bugs/issue-5a10ec7298127df3c62255ea59e01dcf831ff1d3.yaml
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/bugs/issue-67f704f8b7190ccc1157eec007c3d584779dc805.yaml
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/bugs/issue-881ae950569b6ca718fae0060f2751710b972fd2.yaml
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/bugs/issue-bc8dfdf3834bb84b1d942ab2a90ac8c82b4389fb.yaml
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/bugs/issue-d05e9a907202348d47c4bf92062c1f4673dcae68.yaml
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/bugs/issue-f30a3db19d917f8e72ca8689e099ef0cb2681fd3.yaml
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/bugs/project.yaml
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/construct.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/geminstaller.yml
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/lib/construct.rb
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/lib/construct/helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/lib/construct/path_extensions.rb
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/tasks/ann.rake
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/tasks/bones.rake
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/tasks/gem.rake
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/tasks/git.rake
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/tasks/notes.rake
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/tasks/post_load.rake
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/tasks/rdoc.rake
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/tasks/rubyforge.rake
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/tasks/setup.rb
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/tasks/spec.rake
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/tasks/svn.rake
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/tasks/test.rake
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/tasks/zentest.rake
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/test/#construct_test.rb#
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/test/construct_test.rb
/usr/lib64/ruby/gems/2.3.0/gems/test-construct-1.2.2/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/test-construct-1.2.2.gemspec
