ARG IMAGE="ubuntu"

ARG VARIANT="24.04"

FROM ${IMAGE}:${VARIANT}

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    fish \
    git \
    git-lfs \
    gpg \
    htop \
    sudo \
    tmux \
    wget \
    && curl -fsSL https://dl.google.com/linux/linux_signing_key.pub| sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/google.gpg \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && wget -O- https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB | gpg --dearmor | sudo tee /usr/share/keyrings/oneapi-archive-keyring.gpg > /dev/null \
    && echo "deb [signed-by=/usr/share/keyrings/oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi all main" | sudo tee /etc/apt/sources.list.d/oneAPI.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    google-chrome-stable \
    intel-oneapi-mkl \
    intel-oneapi-mkl-devel \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/*

# user
ARG USER_NAME="vscode"

ARG GROUP_NAME="vscode"

ARG USER_UID="1111"

ARG USER_GID=${USER_UID}

RUN groupadd -g ${USER_GID} ${GROUP_NAME} \
    && useradd -u ${USER_UID} -g ${USER_GID} -m ${USER_NAME} \
    && echo ${USER_NAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USER_NAME} \
    && chmod 0440 /etc/sudoers.d/${USER_NAME}

# make directory for extension
RUN mkdir -p /home/${USER_NAME}/.vscode-server/extensions \
        /home/${USER_NAME}/.vscode-server-insiders/extensions \
    && chown -R ${USER_NAME} \
        /home/${USER_NAME}/.vscode-server \
        /home/${USER_NAME}/.vscode-server-insiders

# install rye
USER ${USER_NAME}

# ARG RYE_HOME="~/.rye"

# ENV RYE_HOME=${RYE_HOME}

RUN curl -sSf https://rye.astral.sh/get | RYE_INSTALL_OPTION="--yes" bash

# ENV PATH="$RYE_HOME/shims:$PATH"

CMD ["/bin/bash"]