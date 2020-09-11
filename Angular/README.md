Angular

https://material.angular.io/components/categories

Divider, Slider, Icon, List

# Next, you can login as ordinary user.
# Node Version Manager - NVM is essential for Angular App building
# For a fully manual install, execute the following lines to first$
# and then load nvm:

export NVM_DIR="$HOME/.nvm" && (
git clone https://github.com/nvm-sh/nvm.git "$NVM_DIR"
cd "$NVM_DIR"
git checkout `git describe --abbrev=0 --tags --match "v[0-9]*" $(git rev-list --tags --max-count=1)`
) && \. "$NVM_DIR/nvm.sh"


# Install actual node version:
nvm i 12


# Verify the NODE version by:
node -v  # Should be like 12.x.x


# Verify the NPM version by:
npm -v  # Should be like 6.x.x


# Lastly, add these lines to your ~/.bashrc, ~/.profile,
# or ~/.zshrc file to have it automatically sourced upon
# login or opening a new terminal.

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm


# Finally install Angular
npm install -g @angular/cli


# Create new application
ng new MyApp

# Add angular material
ng add @angular/material
